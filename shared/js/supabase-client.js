/**
 * Educamob Escola Digital - Supabase Client
 * Módulo central de conexão com o banco de dados e autenticação.
 */

// ⚠️ ATENÇÃO: Substitua pelas chaves reais do seu projeto Supabase
const SUPABASE_URL = 'https://jaaiyectjtmlymcjzgpb.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImphYWl5ZWN0anRtbHltY2p6Z3BiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzk4Mjk1MzksImV4cCI6MjA5NTQwNTUzOX0.g9x-e9IEvOGe0CfW6obz2aZ5j-rwx1ugNfRx9KNVIP4';

if (!window.supabase) {
    console.error("SDK do Supabase não carregado. Verifique a tag <script> no HTML.");
} else {
    // Inicializa o cliente e o deixa disponível globalmente para os outros scripts
    window.supabaseClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
    console.log("Supabase Client inicializado com sucesso.");
}
