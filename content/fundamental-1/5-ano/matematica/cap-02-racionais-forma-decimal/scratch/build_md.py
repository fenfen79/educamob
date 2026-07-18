import os
import sys

# Import questions from part1, part2, part3
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from part1 import get_q_basicas
from part2 import get_q_intermediarias
from part3 import get_q_dificeis

def generate_markdown():
    frontmatter = """---
série: "5º Ano"
disciplina: "Matemática"
objeto_de_conhecimento: "Números racionais expressos na forma decimal e sua representação na reta numérica"
ebook_fonte: "ef05ma02.md"
habilidades: "EF05MA02"
total_exercicios: 60
distribuicao:
  basico: 20
  intermediario: 20
  dificil: 20
---

# Exercícios — Números Racionais na Forma Decimal e sua Representação na Reta Numérica
"""

    md_content = frontmatter
    
    questions = get_q_basicas() + get_q_intermediarias() + get_q_dificeis()
    
    # Process Basico
    md_content += "\n## Nível Básico (Questões 1-20)\n\n"
    for i in range(20):
        md_content += format_question(questions[i], i+1)
        
    # Process Intermediario
    md_content += "\n## Nível Intermediário (Questões 21-40)\n\n"
    for i in range(20, 40):
        md_content += format_question(questions[i], i+1)
        
    # Process Dificil
    md_content += "\n## Nível Difícil (Questões 41-60)\n\n"
    for i in range(40, 60):
        md_content += format_question(questions[i], i+1)

    return md_content

def format_question(q, num):
    # <!-- id: q01 | tipo: multipla-escolha | habilidade: EF05MA02 | dificuldade: basico | objeto: racionais-forma-decimal -->
    q_id_str = f"q{num:02d}"
    habilidade = "EF05MA02"
    dificuldade = q["dificuldade"]
    slug = "racionais-forma-decimal"
    
    tag = f"<!-- id: {q_id_str} | tipo: multipla-escolha | habilidade: {habilidade} | dificuldade: {dificuldade} | objeto: {slug} -->"
    
    alts = "\n".join(q["alternativas"])
    
    return f"{tag}\n### Questão {num}\n{q['enunciado']}\n\n{alts}\n\n**Gabarito:** {q['gabarito']}\n**Resolução:** {q['resolucao']}\n\n"

if __name__ == "__main__":
    final_md = generate_markdown()
    out_path = r"c:\Users\nepov\Documents\Pessoal\Antigravity\🚀 Educamob - DevOps e Infra\content\fundamental-1\5-ano\matematica\cap-02-racionais-forma-decimal\ebooks\ef05ma02-exercicios.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(final_md)
    print("Arquivo ef05ma02-exercicios.md gerado com sucesso!")
