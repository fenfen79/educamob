import asyncio
from supabase.client import create_async_client
import os
from dotenv import load_dotenv
load_dotenv()
async def main():
    supabase = await create_async_client(os.getenv('SUPABASE_URL'), 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImphYWl5ZWN0anRtbHltY2p6Z3BiIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3OTgyOTUzOSwiZXhwIjoyMDk1NDA1NTM5fQ.I-ySoCJqIQnbjx3xUuVZVP2C9xht8kosQcPIykPhBOs')
    msgs = await supabase.table('messages').select('*').eq('session_id', '718249b6-8500-4e3c-adfb-4ddcd06e835d').order('created_at', desc=False).execute()
    with open('test_msgs.txt', 'w', encoding='utf-8') as f:
        for m in msgs.data:
            f.write(f"\n--- {m['role'].upper()} ---\n")
            f.write(m['content'])
asyncio.run(main())
