import os
import csv
import re
from supabase.client import Client, create_client
import supabase._sync.client

# Patch para contornar a validação regex do Supabase Client para chaves não-JWT
original_match = re.match
def patched_match(pattern, string, flags=0):
    if pattern == r"^[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*$":
        return True
    return original_match(pattern, string, flags)
supabase._sync.client.re.match = patched_match

from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("ERRO: As chaves do Supabase não foram encontradas no .env")
    exit(1)

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

CSV_PATH = "beta_testers.csv"

def importar_usuarios():
    if not os.path.exists(CSV_PATH):
        print(f"ERRO: Arquivo '{CSV_PATH}' não encontrado.")
        print("Crie um arquivo 'beta_testers.csv' com as colunas: Nome,E-mail,Série,Data de nascimento")
        return
        
    sucessos = 0
    falhas = 0
    
    with open(CSV_PATH, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # Pega as chaves reais que estão no CSV gerado
            nome = row.get("Nome", "").strip()
            email = row.get("E-mail", "").strip()
            serie = row.get("Série", row.get("S\xc3\xa9rie", "")).strip()  # lidando com possíveis falhas de encoding
            nascimento = row.get("Data de nascimento", "").strip()
            
            if not email:
                continue
                
            # Limpar a data de nascimento caso tenha barras (ex: 15/08/2005 vira 15082005)
            # O Supabase exige no mínimo 6 caracteres para a senha
            senha = nascimento.replace("/", "").replace("-", "")
            
            if len(senha) < 6:
                print(f"⚠️ A senha (data de nascimento) para {email} é muito curta ou não informada. Pulando.")
                falhas += 1
                continue
            
            try:
                # Usa admin.create_user para contornar rate limits (requer service_role key)
                res = supabase.auth.admin.create_user({
                    "email": email,
                    "password": senha,
                    "email_confirm": True,
                    "user_metadata": {
                        "full_name": nome,
                        "serie": serie
                    }
                })
                
                print(f"✅ Conta criada: {email} | Senha configurada via Data de Nascimento")
                sucessos += 1
                import time
                time.sleep(1)
                
            except Exception as e:
                msg = str(e)
                if "User already registered" in msg:
                    print(f"⚠️ Conta já existe: {email}")
                else:
                    print(f"❌ Erro ao criar {email}: {msg}")
                falhas += 1
                
    print(f"\n--- RESUMO DA IMPORTAÇÃO ---")
    print(f"Total Sucessos: {sucessos}")
    print(f"Total Falhas/Duplicados: {falhas}")

if __name__ == "__main__":
    print("Iniciando importação de usuários Beta...")
    importar_usuarios()
