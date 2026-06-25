/**
 * Educamob Escola Digital - Auth Guard
 * Protege as rotas privadas. Deve ser incluído após o supabase-client.js
 */

(async function() {
    if (!window.supabaseClient) {
        console.error("Supabase client não encontrado. O Auth Guard precisa do supabase-client.js carregado antes dele.");
        return;
    }

    // Se as chaves ainda não foram configuradas, não faremos o bloqueio rígido 
    // para evitar tela branca em desenvolvimento (antes da inserção das chaves).
    if (SUPABASE_URL.includes('COLE_AQUI')) {
        console.warn("Auth Guard Desativado: Chaves do Supabase não configuradas.");
        return;
    }

    const { data, error } = await window.supabaseClient.auth.getSession();
    
    if (error || !data.session) {
        console.log("Acesso Negado: Usuário não autenticado. Redirecionando...");
        // Como todos os apps estão na pasta /apps/, o caminho ../login/index.html funciona.
        window.location.href = '../login/index.html';
    } else {
        console.log("Acesso Liberado: Sessão válida encontrada.");
    }
})();
