document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const recoveryForm = document.getElementById('recovery-form');
    const resetPasswordForm = document.getElementById('reset-password-form');
    
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const recoveryEmailInput = document.getElementById('recovery-email');
    const newPasswordInput = document.getElementById('new-password');

    const errorMessage = document.getElementById('error-message');
    const btnText = document.getElementById('btn-text');
    const btnLoader = document.getElementById('btn-loader');
    const btnSubmit = document.getElementById('btn-submit');
    const btnRecoverySubmit = document.getElementById('btn-recovery-submit');
    const btnResetSubmit = document.getElementById('btn-reset-submit');

    const forgotPasswordLink = document.getElementById('forgot-password-link');
    const backToLoginLink = document.getElementById('back-to-login');

    // Se as chaves do Supabase não foram configuradas
    if (SUPABASE_URL.includes('COLE_AQUI')) {
        showError("⚠️ Sistema em Manutenção. O banco de dados (Supabase) ainda não foi conectado. Insira as chaves no código.");
        emailInput.disabled = true;
        passwordInput.disabled = true;
        btnSubmit.disabled = true;
        return;
    }

    // Listener global para detectar clique no link do email (Recuperação de Senha)
    window.supabaseClient.auth.onAuthStateChange(async (event, session) => {
        if (event == "PASSWORD_RECOVERY") {
            // O aluno clicou no link do e-mail. Vamos mostrar apenas a tela de digitar nova senha.
            hideError();
            loginForm.style.display = 'none';
            recoveryForm.style.display = 'none';
            resetPasswordForm.style.display = 'block';
            document.querySelector('.login-subtitle').textContent = "Recuperação de Senha Segura";
        }
    });

    // Verificar se já está logado
    const checkSession = async () => {
        // Se a url tiver #access_token, o onAuthStateChange vai pegar, então não redirecionamos direto se for recuperação
        if (window.location.hash.includes('type=recovery')) {
            return;
        }

        const { data, error } = await window.supabaseClient.auth.getSession();
        if (data && data.session) {
            window.location.href = '../dashboard/index.html';
        }
    };
    checkSession();

    function showError(msg) {
        errorMessage.textContent = msg;
        errorMessage.style.display = 'block';
    }

    function hideError() {
        errorMessage.style.display = 'none';
    }

    function setLoading(isLoading) {
        if (isLoading) {
            btnText.style.display = 'none';
            btnLoader.style.display = 'block';
            btnSubmit.disabled = true;
            emailInput.disabled = true;
            passwordInput.disabled = true;
        } else {
            btnText.style.display = 'block';
            btnLoader.style.display = 'none';
            btnSubmit.disabled = false;
            emailInput.disabled = false;
            passwordInput.disabled = false;
        }
    }

    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        hideError();
        
        const email = emailInput.value.trim();
        const password = passwordInput.value.trim();

        if (!email || !password) {
            showError("Preencha e-mail e senha para acessar.");
            return;
        }

        setLoading(true);

        // Chamada de Autenticação no Supabase
        const { data, error } = await window.supabaseClient.auth.signInWithPassword({
            email: email,
            password: password,
        });

        if (error) {
            setLoading(false);
            if (error.message.includes('Invalid login credentials')) {
                showError("E-mail ou senha incorretos.");
            } else {
                showError("Erro ao fazer login: " + error.message);
            }
        } else {
            window.location.href = '../dashboard/index.html';
        }
    });

    // --- NAVEGAÇÃO ENTRE TELAS ---
    forgotPasswordLink.addEventListener('click', (e) => {
        e.preventDefault();
        hideError();
        loginForm.style.display = 'none';
        recoveryForm.style.display = 'block';
        document.querySelector('.login-subtitle').textContent = "Recupere seu acesso";
    });

    backToLoginLink.addEventListener('click', (e) => {
        e.preventDefault();
        hideError();
        recoveryForm.style.display = 'none';
        loginForm.style.display = 'block';
        document.querySelector('.login-subtitle').textContent = "Acesse o seu portal de estudos";
    });

    // --- ENVIAR EMAIL DE RECUPERAÇÃO ---
    recoveryForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        hideError();
        
        const email = recoveryEmailInput.value.trim();
        if (!email) {
            showError("Preencha o e-mail cadastrado.");
            return;
        }

        const btnTextEl = document.getElementById('btn-recovery-text');
        btnTextEl.textContent = "Enviando...";
        btnRecoverySubmit.disabled = true;

        const { data, error } = await window.supabaseClient.auth.resetPasswordForEmail(email, {
            redirectTo: window.location.href, // Redireciona de volta pra essa mesma tela após clicar no email
        });

        if (error) {
            showError("Erro: " + error.message);
            btnTextEl.textContent = "Enviar Link Seguro";
            btnRecoverySubmit.disabled = false;
        } else {
            // Sucesso
            errorMessage.textContent = "Se este e-mail estiver cadastrado, você receberá um link em instantes. Verifique sua caixa de entrada e spam.";
            errorMessage.style.backgroundColor = "rgba(76, 175, 80, 0.1)";
            errorMessage.style.borderColor = "rgba(76, 175, 80, 0.3)";
            errorMessage.style.color = "#4caf50";
            errorMessage.style.display = 'block';
            
            btnTextEl.textContent = "E-mail Enviado!";
        }
    });

    // --- SALVAR A NOVA SENHA ---
    resetPasswordForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        hideError();

        const newPass = newPasswordInput.value.trim();
        if (newPass.length < 6) {
            showError("A senha precisa ter pelo menos 6 caracteres.");
            return;
        }

        const btnTextEl = document.getElementById('btn-reset-text');
        btnTextEl.textContent = "Salvando...";
        btnResetSubmit.disabled = true;

        const { data, error } = await window.supabaseClient.auth.updateUser({
            password: newPass
        });

        if (error) {
            showError("Erro ao salvar senha: " + error.message);
            btnTextEl.textContent = "Salvar e Entrar";
            btnResetSubmit.disabled = false;
        } else {
            // Senha trocada com sucesso, joga pro dashboard!
            window.location.href = '../dashboard/index.html';
        }
    });
});
