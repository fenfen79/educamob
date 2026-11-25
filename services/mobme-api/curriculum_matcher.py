import os
import json
import re
import unicodedata
from dataclasses import dataclass
from typing import Optional, List, Dict, Any

def clean_text(text: str) -> str:
    if not text:
        return ""
    norm = unicodedata.normalize("NFD", text.lower())
    return "".join(c for c in norm if unicodedata.category(c) != "Mn").strip()

def stem_pt(w: str) -> str:
    if w.endswith("oes"):
        return w[:-3] + "ao"
    elif w.endswith("s") and len(w) > 3 and not w.endswith("ss"):
        return w[:-1]
    return w

def tokenize(text: str) -> list[str]:
    cleaned = clean_text(text)
    # Suporta normalização de ordinais universais: 1o, 1ª, 1º -> 1
    cleaned = re.sub(r'\b(1o|1a|1º|1ª|primeiro|primeira)\b', '1', cleaned)
    cleaned = re.sub(r'\b(2o|2a|2º|2ª|segundo|segunda)\b', '2', cleaned)
    cleaned = re.sub(r'\b(3o|3a|3º|3ª|terceiro|terceira)\b', '3', cleaned)
    raw_tokens = [w for w in re.findall(r'[a-z0-9]+', cleaned) if len(w) > 1 or w in {'1', '2', '3'}]
    return [stem_pt(w) for w in raw_tokens]

STOPWORDS = {
    "de", "da", "do", "das", "dos", "em", "para", "com", "por", "sobre",
    "um", "uma", "uns", "umas", "o", "a", "os", "as", "e", "ou", "se",
    "que", "como", "nao", "mais", "seu", "sua", "seus", "suas", "pela", "pelo",
    "quero", "estudar", "ajuda", "me", "explicar", "conteudo", "materia", "assunto",
    "aula", "tema", "saber", "fale", "ver", "exercicio", "exercicios", "acho", "acha",
    "encontro", "calcular", "calcula", "resolva", "resolve", "qual", "quanto", "quantos"
}

QUESTION_MARKERS = {
    "como", "por que", "porque", "qual", "quais", "quanto", "quantos", "onde",
    "quando", "quem", "o que", "oque", "me ajuda", "me explica", "pode explicar"
}

@dataclass
class MatchResult:
    is_match: bool
    is_broad: bool
    canonical_topic: Optional[str] = None
    discipline: Optional[str] = None
    grade: Optional[str] = None
    ebook_path: Optional[str] = None
    exercise_path: Optional[str] = None
    chapter_id: Optional[str] = None
    score: float = 0.0
    options: Optional[List[str]] = None
    clean_names: Optional[List[str]] = None
    reason: Optional[str] = None

class CurriculumMatcher:
    def __init__(self, catalog_path: str = None):
        if not catalog_path:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            catalog_path = os.path.join(current_dir, "curriculum_catalog.json")
        self.catalog_path = catalog_path
        self.catalog: List[Dict[str, Any]] = []
        self.inverted_index: Dict[str, List[int]] = {}
        self.load_catalog()

    def load_catalog(self):
        if not os.path.exists(self.catalog_path):
            from build_catalog import build_catalog
            project_root = os.path.abspath(os.path.join(os.path.dirname(self.catalog_path), "..", ".."))
            content_dir = os.path.join(project_root, "content")
            self.catalog = build_catalog(content_dir, self.catalog_path)
        else:
            with open(self.catalog_path, "r", encoding="utf-8") as f:
                self.catalog = json.load(f)

        self.inverted_index = {}
        for idx, entry in enumerate(self.catalog):
            all_tokens = set(tokenize(entry["canonical_topic"]))
            all_tokens.update(tokenize(entry["h1_title"]))
            for kw in entry.get("keywords", []):
                all_tokens.update(tokenize(kw))
            all_tokens.update(tokenize(entry.get("discipline", "")))
            
            for token in all_tokens:
                if token not in STOPWORDS:
                    self.inverted_index.setdefault(token, []).append(idx)

    def match(self, query: str, user_grade: str = None, session_discipline: str = None) -> MatchResult:
        q_tokens = [t for t in tokenize(query) if t not in STOPWORDS]
        if not q_tokens:
            return MatchResult(is_match=False, is_broad=False)

        candidate_scores: Dict[int, float] = {}
        q_token_set = set(q_tokens)
        
        has_ord1 = '1' in q_token_set
        has_ord2 = '2' in q_token_set
        has_ord3 = '3' in q_token_set

        for t in q_tokens:
            postings = self.inverted_index.get(t, [])
            for idx in postings:
                candidate_scores[idx] = candidate_scores.get(idx, 0.0) + 1.0

        if not candidate_scores:
            return MatchResult(is_match=False, is_broad=False)

        scored_candidates = []
        for idx, base_score in candidate_scores.items():
            entry = self.catalog[idx]
            score = 0.0
            
            raw_title_tokens = tokenize(entry["canonical_topic"])
            title_tokens = set(raw_title_tokens)
            h1_tokens = set(tokenize(entry["h1_title"]))
            entry_tokens = set(entry.get("tokens", []))
            disc_clean = clean_text(entry.get("discipline", ""))
            
            for pos, qt in enumerate(q_tokens):
                if qt in title_tokens:
                    # Bônus de relevância: palavras no início do título têm peso maior
                    idx_in_title = raw_title_tokens.index(qt) if qt in raw_title_tokens else 10
                    pos_bonus = max(1.0, 3.0 - (idx_in_title * 0.3))
                    score += 5.0 * pos_bonus
                elif qt in h1_tokens:
                    score += 4.0
                elif qt in entry_tokens:
                    score += 2.0
                elif qt in disc_clean:
                    score += 1.5

            clean_q = clean_text(query)
            clean_title = clean_text(entry["canonical_topic"])
            clean_h1 = clean_text(entry["h1_title"])
            if clean_q in clean_title or clean_title in clean_q:
                score += 8.0
            elif clean_q in clean_h1 or clean_h1 in clean_q:
                score += 6.0

            # Penalidade de ordinal conflitante (1 vs 2 vs 3)
            entry_ord1 = '1' in title_tokens or '1' in h1_tokens
            entry_ord2 = '2' in title_tokens or '2' in h1_tokens
            entry_ord3 = '3' in title_tokens or '3' in h1_tokens

            if has_ord1 and not entry_ord1 and (entry_ord2 or entry_ord3):
                score -= 15.0
            if has_ord2 and not entry_ord2 and (entry_ord1 or entry_ord3):
                score -= 15.0
            if has_ord3 and not entry_ord3 and (entry_ord1 or entry_ord2):
                score -= 15.0

            # Bônus / Penalidade de disciplina
            if session_discipline:
                s_disc_clean = clean_text(session_discipline)
                if s_disc_clean in disc_clean or disc_clean in s_disc_clean:
                    score += 6.0
                else:
                    score -= 6.0

            # Bônus de série / segmento
            if user_grade:
                ug_clean = clean_text(user_grade)
                entry_grade = clean_text(entry.get("grade", ""))
                if ("medio" in ug_clean and "medio" in entry_grade) or ("fundamental" in ug_clean and "fundamental" in entry_grade):
                    score += 2.0

            if score > 0:
                scored_candidates.append((score, entry))

        scored_candidates.sort(key=lambda x: x[0], reverse=True)
        if not scored_candidates:
            return MatchResult(is_match=False, is_broad=False)

        top_score, top_entry = scored_candidates[0]
        if top_score < 4.0:
            return MatchResult(is_match=False, is_broad=False)

        # Checagem de Desambiguação Orgânica
        distinct_top = []
        seen_keys = set()
        for sc, ent in scored_candidates:
            if sc >= (top_score * 0.70) and sc >= 5.0:
                key = (ent["discipline"], ent["canonical_topic"])
                if key not in seen_keys:
                    seen_keys.add(key)
                    distinct_top.append(ent)
            if len(distinct_top) >= 4:
                break

        if len(distinct_top) >= 2 and len(q_tokens) <= 2 and (scored_candidates[1][0] >= top_score - 3.0):
            options = []
            clean_names = []
            for d_ent in distinct_top:
                topic_name = d_ent["canonical_topic"]
                disc_name = d_ent["discipline"]
                kw_hint = ", ".join(d_ent.get("keywords", [])[:3])
                desc = f"**{topic_name}** ({disc_name}: {kw_hint})" if kw_hint else f"**{topic_name}** ({disc_name})"
                options.append(desc)
                clean_names.append(topic_name)

            return MatchResult(
                is_match=True,
                is_broad=True,
                canonical_topic=query.capitalize(),
                discipline="Interdisciplinar" if len(set(d["discipline"] for d in distinct_top)) > 1 else distinct_top[0]["discipline"],
                score=top_score,
                options=options,
                clean_names=clean_names,
                reason="MULTIPLE_CURRICULAR_CHAPTERS"
            )

        return MatchResult(
            is_match=True,
            is_broad=False,
            canonical_topic=top_entry["canonical_topic"],
            discipline=top_entry["discipline"],
            grade=top_entry["grade"],
            ebook_path=top_entry["ebook_path"],
            exercise_path=top_entry["exercise_path"],
            chapter_id=top_entry["id"],
            score=top_score
        )

    def is_different_topic(self, current_topic: str, new_message: str, current_discipline: str = None) -> bool:
        """
        Determina se new_message expressa a intenção de trocar para um capítulo curricular
        distinto do current_topic da sessão monotemática.
        """
        if not current_topic or not new_message:
            return False

        msg_clean = clean_text(new_message)

        # 1. Comandos de controle, trilhas ou respostas isoladas NUNCA são troca de assunto
        if msg_clean in {"menu", "o menu", "voltar", "pausa", "continuar", "finalizar", "encerrar"} or msg_clean in {"1", "2", "3", "4", "5", "6"}:
            return False
        if any(msg_clean.startswith(f"{n}.") for n in ["1", "2", "3", "4", "5", "6"]):
            return False

        # 2. Perguntas pontuais de dúvida ou exercícios ("como acho...", "qual é a formula...") NUNCA são troca de assunto
        if msg_clean.endswith("?") or any(msg_clean.startswith(qm) for qm in QUESTION_MARKERS):
            return False

        # 3. Match contra o catálogo
        res = self.match(new_message, session_discipline=current_discipline)
        if not res.is_match:
            return False

        # Se o score for baixo ou difuso, não força troca
        if res.score < 6.0:
            return False

        curr_clean = clean_text(current_topic)
        new_clean = clean_text(res.canonical_topic or "")

        if curr_clean == new_clean:
            return False

        # Conflito explícito de ordinais (1º grau vs 2º grau)
        c_ord1 = '1' in tokenize(current_topic)
        c_ord2 = '2' in tokenize(current_topic)
        n_ord1 = '1' in tokenize(res.canonical_topic or "")
        n_ord2 = '2' in tokenize(res.canonical_topic or "")

        if (c_ord1 and n_ord2) or (c_ord2 and n_ord1):
            return True

        # Se for na mesma disciplina e houver sobreposição de termos, não é troca
        if current_discipline and res.discipline and current_discipline.lower() == res.discipline.lower():
            c_tokens = set(tokenize(current_topic)) - STOPWORDS
            n_tokens = set(tokenize(res.canonical_topic or "")) - STOPWORDS
            if len(c_tokens.intersection(n_tokens)) >= 2:
                return False

        if new_clean in curr_clean or curr_clean in new_clean:
            return False

        return True

curriculum_matcher = CurriculumMatcher()
