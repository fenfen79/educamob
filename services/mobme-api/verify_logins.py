import os
import csv
import re
import supabase._sync.client
import time

original_match = re.match
def patched_match(pattern, string, flags=0):
    if "A-Za-z0-9-_=" in pattern:
        return True
    return original_match(pattern, string, flags)
supabase._sync.client.re.match = patched_match

from supabase.client import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
CSV_PATH = 'beta_testers.csv'

sucessos = 0
falhas = 0

with open(CSV_PATH, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        email = row.get('E-mail', '').strip()
        nascimento = row.get('Data de nascimento', '').strip()
        if not email:
            continue
        senha = nascimento.replace('/', '').replace('-', '')
        
        try:
            res = supabase.auth.sign_in_with_password({'email': email, 'password': senha})
            if res.user:
                print(f'✅ OK: {email}')
                sucessos += 1
            time.sleep(1) # para evitar rate limit
        except Exception as e:
            print(f'❌ FALHA {email}: {str(e)}')
            falhas += 1
            time.sleep(1)

print(f'\nTotal OK: {sucessos} | Total Falhas: {falhas}')
