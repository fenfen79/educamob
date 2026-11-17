import re

def fix_draft():
    draft_path = r"c:\Users\nepov\Documents\Pessoal\Antigravity\🚀 Educamob - DevOps e Infra\temp_draft_c50.md"
    with open(draft_path, "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Ajustar Etapas nas resoluções: de "**Etapa 1: Algo:**" para "**Etapa 1:** Algo:"
    text = re.sub(r'\*\*(Etapa \d+):\s*([^:\*]+):\*\*', r'**\1:** \2:', text)
    # Também qualquer caso onde ficou "**Etapa 1: Algo"
    text = re.sub(r'\*\*(Etapa \d+):([^\*]+)\*\*', r'**\1:**\2', text)

    # 2. Corrigir entidades fora do e-book:
    # Q46: Decreto-Lei
    text = text.replace("o Decreto-Lei nº 294 tornou", "em 1938 Vargas tornou")
    text = text.replace("Decreto-Lei", "determinação oficial")

    # Q47: Afro-Brasileiras
    text = text.replace("manifestações afro-brasileiras", "manifestações populares do samba")
    text = text.replace("Afro-Brasileiras", "Cariocas")
    text = text.replace("afro-brasileiras", "do samba carioca")

    # Q48: Meio-Oeste
    text = text.replace("cidades do Meio-Oeste", "cidades norte-americanas")
    text = text.replace("Meio-Oeste", "interior dos Estados Unidos")

    # 3. Remover termos de concursês (auferir, hegemônico)
    text = text.replace("auferir", "obter")
    text = text.replace("hegemônico", "dominante")
    text = text.replace("hegemônica", "dominante")
    text = text.replace("Hegemônico", "Dominante")
    text = text.replace("Hegemônica", "Dominante")
    # Caso ainda haja alguma variação
    text = re.sub(r'\bhegem[ôo]nic[oa]s?\b', 'dominante', text, flags=re.IGNORECASE)

    with open(draft_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("temp_draft_c50.md updated with fixes!")

if __name__ == "__main__":
    fix_draft()
