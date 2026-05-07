document.addEventListener('DOMContentLoaded', () => {

    // 1. Scroll Reveal Logic
    const revealElements = document.querySelectorAll('.scroll-reveal');
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, { threshold: 0.1 });

    revealElements.forEach(el => revealObserver.observe(el));

    // 2. Quiz Interaction Logic
    const quizCards = document.querySelectorAll('.quiz-card');

    quizCards.forEach(card => {
        const buttons = card.querySelectorAll('.opt-btn');
        const explanation = card.querySelector('.explanation');

        buttons.forEach(btn => {
            btn.addEventListener('click', () => {
                const isCorrect = btn.getAttribute('data-correct') === 'true';

                // Disable all options in this card
                buttons.forEach(b => {
                    b.classList.add('disabled');
                    if (b.getAttribute('data-correct') === 'true') {
                        b.classList.add('correct');
                    }
                });

                if (isCorrect) {
                    btn.classList.add('correct');
                } else {
                    btn.classList.add('wrong');
                    if (explanation) {
                        explanation.classList.remove('hidden');
                    }
                }
            });
        });
    });

    // 3. Smooth Scroll for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
