document.addEventListener('DOMContentLoaded', () => {

    // 1. Scroll Reveal Animation
    const revealElements = document.querySelectorAll('.scroll-reveal');
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    revealElements.forEach(el => revealObserver.observe(el));

    // 2. Quiz Logic with block feedback
    const quizCards = document.querySelectorAll('.quiz-card');
    const blockScores = {};

    quizCards.forEach(card => {
        const buttons = card.querySelectorAll('.opt-btn');
        const explanation = card.querySelector('.explanation');
        const blockId = card.closest('.quiz-container')?.dataset.block;

        if (blockId && !blockScores[blockId]) {
            blockScores[blockId] = { total: 0, correct: 0 };
        }
        if (blockId) {
            blockScores[blockId].total++;
        }

        buttons.forEach(btn => {
            btn.addEventListener('click', () => {
                // Disable all buttons
                buttons.forEach(b => {
                    b.classList.add('disabled');
                    b.setAttribute('disabled', true);
                });

                const isCorrect = btn.dataset.correct === 'true';

                if (isCorrect) {
                    btn.classList.add('correct');
                    if (blockId) blockScores[blockId].correct++;
                    if (explanation) {
                        explanation.classList.remove('hidden');
                        explanation.classList.add('success-msg');
                    }
                } else {
                    btn.classList.add('wrong');
                    // Highlight correct answer
                    buttons.forEach(b => {
                        if (b.dataset.correct === 'true') b.classList.add('correct');
                    });
                    if (explanation) {
                        explanation.classList.remove('hidden');
                        explanation.classList.add('error-msg');
                    }
                }

                // Check if all questions in block answered
                if (blockId) {
                    checkBlockComplete(blockId);
                }

                // Update global dashboard tracking
                updateSPADashboard();
            });
        });
    });

    function checkBlockComplete(blockId) {
        const container = document.querySelector(`[data-block="${blockId}"]`);
        if (!container) return;
        const allCards = container.querySelectorAll('.quiz-card');
        const answeredCards = container.querySelectorAll('.quiz-card .opt-btn.disabled');

        // Count how many cards have been answered (at least one disabled button per card)
        let answeredCount = 0;
        allCards.forEach(card => {
            const hasDisabled = card.querySelector('.opt-btn.disabled');
            if (hasDisabled) answeredCount++;
        });

        if (answeredCount === allCards.length) {
            const feedbackEl = container.querySelector('.block-feedback');
            if (!feedbackEl) return;

            const score = blockScores[blockId];
            const pct = (score.correct / score.total) * 100;

            if (pct >= 70) {
                feedbackEl.textContent = 'Mandou Bem! 👍🏾 (' + score.correct + '/' + score.total + ')';
                feedbackEl.classList.add('good');
            } else {
                feedbackEl.textContent = 'Vamos Melhorar? 💪🏾 (' + score.correct + '/' + score.total + ')';
                feedbackEl.classList.add('improve');
            }
            feedbackEl.classList.add('show');
        }
    }

    // 3. Global Tracking for Dashboard
    async function updateSPADashboard() {
        let totalQuestions = document.querySelectorAll('.quiz-card').length;
        let answeredCards = 0;
        let correctCards = 0;

        document.querySelectorAll('.quiz-card').forEach(card => {
            let isAnswered = false;
            card.querySelectorAll('.opt-btn').forEach(b => { 
                if (b.classList.contains('disabled')) isAnswered = true; 
            });
            
            if (isAnswered) {
                answeredCards++;
                const hasWrong = card.querySelector('.opt-btn.wrong');
                if (!hasWrong) {
                    correctCards++;
                }
            }
        });

        const state = {
            currentQuestionIndex: answeredCards,
            totalQuestions: totalQuestions,
            correctCount: correctCards,
            finished: answeredCards === totalQuestions,
            timestamp: Date.now(),
            type: "spa" // Identificador para o Dashboard
        };

        localStorage.setItem('educamob_spa_matematica_8_monomios', JSON.stringify(state));

        // Envio para a Nuvem (Supabase)
        if (state.finished && window.supabaseClient) {
            try {
                const { data: { session } } = await window.supabaseClient.auth.getSession();
                if (session) {
                    const score = state.totalQuestions > 0 ? (state.correctCount / state.totalQuestions) * 100 : 0;
                    const { error } = await window.supabaseClient.from('student_progress').insert([
                        {
                            user_id: session.user.id,
                            subject_id: 'matematica_8_monomios',
                            subject_name: 'Monômios e Polinômios',
                            score: score,
                            total_questions: state.totalQuestions,
                            activity_type: 'spa'
                        }
                    ]);
                    
                    if (error) {
                        console.error("Erro ao salvar no Supabase:", error);
                    } else {
                        console.log("🚀 Nota salva na nuvem com sucesso!");
                    }
                }
            } catch (err) {
                console.error("Erro de conexão com Supabase:", err);
            }
        }
    }
});
