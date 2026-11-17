with open(r"c:\Users\nepov\Documents\Pessoal\Antigravity\🚀 Educamob - DevOps e Infra\temp_draft_c51.md", "r", encoding="utf-8") as f:
    text = f.read()

# Substituir precípua por principal
text = text.replace("tarefa precípua", "tarefa principal")
text = text.replace("precípua", "principal")

# Substituir intrínseca por própria / inerente
text = text.replace("dignidade é intrínseca a todo", "dignidade é inerente a todo")
text = text.replace("intrínseca", "própria")
text = text.replace("intrínseco", "próprio")

with open(r"c:\Users\nepov\Documents\Pessoal\Antigravity\🚀 Educamob - DevOps e Infra\temp_draft_c51.md", "w", encoding="utf-8") as f:
    f.write(text)

print("temp_draft_c51.md updated!")
