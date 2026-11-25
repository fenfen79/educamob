/**
 * Educamob Escola Digital - Supabase Client
 * Módulo central de conexão com o banco de dados e autenticação.
 */

// Chaves Oficiais (Produção)
const PROD_URL = 'https://jaaiyectjtmlymcjzgpb.supabase.co';

// Chaves do Laboratório
const LAB_URL = 'https://fwmbmtmnwlxwbaxzrldp.supabase.co';
const LAB_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ3bWJtdG1ud2x4d2JheHpybGRwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODk3NDIyMjEsImV4cCI6MjEwNTMxODIyMX0.e9N29CHTarEObye819iZqKxfxTe4tn3u0EAluMvLwxk';

let SUPABASE_URL = LAB_URL;
let SUPABASE_ANON_KEY = LAB_KEY;

// Verifica se estamos no Laboratório (Localhost)
const isLocalhost = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';

if (isLocalhost) {
    console.warn("🧪 MODO LABORATÓRIO ATIVADO: Usando Supabase Espelho.");

    // HARD GUARDRAIL: Impede testes locais com banco de produção
    if (SUPABASE_URL === PROD_URL) {
        document.body.innerHTML = "<div style='padding:50px; text-align:center; color:red; font-family:sans-serif;'><h1>🚨 ALERTA CRÍTICO DE SEGURANÇA 🚨</h1><p>Você está tentando rodar o ambiente de desenvolvimento usando o Banco de Dados Oficial da Educamob.</p><p>O carregamento foi bloqueado para proteger as notas dos alunos reais. Configure o <b>env.lab.js</b> com as chaves do Supabase de testes.</p></div>";
        throw new Error("ALERTA CRÍTICO: Tentativa de uso do banco de produção em ambiente local!");
    }
}

if (!window.supabase) {
    console.error("SDK do Supabase não carregado. Verifique a tag <script> no HTML.");
} else {
    // Inicializa o cliente e o deixa disponível globalmente para os outros scripts
    window.supabaseClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
    // FIX: The React chunk expects the initialized client to be at window.supabase
    window.supabase = window.supabaseClient;
    console.log("Supabase Client inicializado com sucesso.");
}
