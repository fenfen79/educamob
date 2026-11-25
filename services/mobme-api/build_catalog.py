import os
import re
import yaml
import json
import unicodedata

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
    raw_tokens = [w for w in re.findall(r'[a-z0-9]+', cleaned) if len(w) > 1]
    return [stem_pt(w) for w in raw_tokens]

def build_catalog(content_dir: str, output_file: str):
    catalog = []
    stopwords = {
        "de", "da", "do", "das", "dos", "em", "para", "com", "por", "sobre",
        "um", "uma", "uns", "umas", "o", "a", "os", "as", "e", "ou", "se",
        "que", "como", "nao", "mais", "seu", "sua", "seus", "suas", "pela", "pelo"
    }

    print(f"Indexando acervo curricular a partir de: {content_dir}...")
    
    for root, dirs, files in os.walk(content_dir):
        ebook_files = [f for f in files if f.endswith(".md") and not f.endswith("-exercicios.md")]
        exercise_files = [f for f in files if f.endswith("-exercicios.md")]
        
        for ef in ebook_files:
            ebook_path = os.path.join(root, ef).replace("\\", "/")
            try:
                with open(ebook_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
            except Exception:
                continue
                
            # Parse YAML Frontmatter
            frontmatter = {}
            if lines and lines[0].strip() == "---":
                yaml_lines = []
                for line in lines[1:]:
                    if line.strip() == "---":
                        break
                    yaml_lines.append(line)
                try:
                    frontmatter = yaml.safe_load("".join(yaml_lines)) or {}
                except Exception:
                    pass
                    
            h1_title = ""
            for line in lines:
                if line.startswith("# "):
                    h1_title = line[2:].strip()
                    break
                    
            obj_conhecimento = frontmatter.get("objeto_de_conhecimento") or h1_title or ef.replace(".md", "").replace("-", " ").title()
            disciplina = frontmatter.get("disciplina") or ""
            serie = frontmatter.get("série") or ""
            unidade = frontmatter.get("unidade_temática") or ""
            palavras_chave = frontmatter.get("palavras_chave") or []
            if isinstance(palavras_chave, str):
                palavras_chave = [p.strip() for p in palavras_chave.split(",")]
                
            if not disciplina:
                parts = ebook_path.lower().split("/")
                for d_cand in ["matematica", "fisica", "quimica", "ciencias", "historia", "geografia", "lingua-portuguesa", "biologia", "filosofia", "sociologia"]:
                    if d_cand in parts:
                        disciplina = d_cand.replace("-", " ").title()
                        break
                        
            matching_ex = None
            if exercise_files:
                base_name = ef.replace(".md", "")
                for exf in exercise_files:
                    if base_name in exf:
                        matching_ex = os.path.join(root, exf).replace("\\", "/")
                        break
                if not matching_ex:
                    matching_ex = os.path.join(root, exercise_files[0]).replace("\\", "/")
                    
            tokens = set()
            for t in tokenize(obj_conhecimento):
                if t not in stopwords:
                    tokens.add(t)
            for kw in palavras_chave:
                for t in tokenize(kw):
                    if t not in stopwords:
                        tokens.add(t)
            for t in tokenize(h1_title):
                if t not in stopwords:
                    tokens.add(t)
                    
            slug = os.path.basename(root)
            
            entry = {
                "id": slug,
                "canonical_topic": obj_conhecimento,
                "h1_title": h1_title,
                "discipline": disciplina,
                "grade": serie,
                "thematic_unit": unidade,
                "keywords": palavras_chave,
                "ebook_path": ebook_path,
                "exercise_path": matching_ex,
                "tokens": list(tokens),
                "raw_search_str": f"{obj_conhecimento} {h1_title} {' '.join(palavras_chave)} {disciplina}".lower()
            }
            catalog.append(entry)
            
    print(f"Total de capítulos indexados: {len(catalog)}")
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
    print(f"Catálogo salvo em: {output_file} ({os.path.getsize(output_file) / 1024:.1f} KB)")
    return catalog

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
    content_dir = os.path.join(project_root, "content")
    output_file = os.path.join(current_dir, "curriculum_catalog.json")
    build_catalog(content_dir, output_file)
