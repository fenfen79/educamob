import os

def append_to_diario():
    with open('diario.md', 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        
    # Limpa possiveis lixos inseridos pelo powershell echo
    clean_lines = [l for l in lines if not '\x00' in l]
    
    with open('diario.md', 'w', encoding='utf-8') as f:
        f.writelines(clean_lines)
        f.write("\n## 10/10/2026 - Injeção Dinâmica de Matérias e Guardião RAG\n")
        f.write("- **Refatoração do Prompt (Mob.me):** O sistema agora conta com uma arquitetura de 'Matérias Dinâmicas'. A IA tem uma restrição explícita (`prompt_prod.md` e `prompt_lab.md`) para não ensinar assuntos que não estejam no banco de dados.\n")
        f.write("- **Injeção de Contexto (FastAPI):** O `main.py` foi atualizado para carregar da tabela `available_subjects` as disciplinas ativas, injetando essa lista no `dynamic_system_prompt` da IA.\n")
        f.write("- **Ingestor Inteligente (Idempotente):** O script `ingest.py` foi completamente refatorado para utilizar hashes locais (`ingest_state.json`), garantindo que apenas arquivos novos ou modificados sejam vetorizados, poupando tokens e tempo. Ele também realiza um `DELETE` cirúrgico no Supabase antes de inserir novos vetores, zerando as duplicatas de e-books na base.\n")

if __name__ == '__main__':
    append_to_diario()
