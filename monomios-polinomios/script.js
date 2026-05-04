document.addEventListener("DOMContentLoaded", () => {
    // 1. Intersection Observer for Scroll Animations
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.fade-in, .scroll-reveal');
    animatedElements.forEach(el => observer.observe(el));

    // 2. Quiz Gamification Logic
    const questions = document.querySelectorAll('.quiz-card');

    questions.forEach(question => {
        const options = question.querySelectorAll('.opt-btn');
        const explanation = question.querySelector('.explanation');

        options.forEach(btn => {
            btn.addEventListener('click', () => {
                // Disable options after click
                options.forEach(b => {
                    b.disabled = true;
                    b.style.cursor = 'not-allowed';
                });

                const isCorrect = btn.getAttribute('data-correct') === 'true';

                if (isCorrect) {
                    btn.classList.add('correct');
                    if (explanation) {
                        explanation.classList.remove('hidden');
                        explanation.classList.add('success-msg');
                        explanation.innerHTML = "<strong>✓ Resposta Correta!</strong> " + explanation.innerHTML;
                    }
                } else {
                    btn.classList.add('wrong');
                    if (explanation) {
                        explanation.classList.remove('hidden');
                        explanation.classList.add('error-msg');
                        explanation.innerHTML = "<strong>✗ Ops, Incorreto.</strong> " + explanation.innerHTML;
                    }

                    // Highlight the correct answer
                    options.forEach(b => {
                        if (b.getAttribute('data-correct') === 'true') {
                            b.classList.add('correct');
                        }
                    });
                }
            });
        });
    });

    // 3. Table of Contents Navigation Dots
    const tocDots = document.querySelectorAll('.toc-dot');
    const sections = [];

    tocDots.forEach(dot => {
        const targetId = dot.getAttribute('data-target');
        const targetEl = document.getElementById(targetId);
        if (targetEl) sections.push({ dot, el: targetEl });

        dot.addEventListener('click', () => {
            if (targetEl) {
                targetEl.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Highlight active section in TOC
    const tocObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                tocDots.forEach(d => d.classList.remove('active'));
                const activeDot = document.querySelector(`.toc-dot[data-target="${entry.target.id}"]`);
                if (activeDot) activeDot.classList.add('active');
            }
        });
    }, { root: null, rootMargin: '-30% 0px -60% 0px', threshold: 0 });

    sections.forEach(s => tocObserver.observe(s.el));

    // 4. Theme Toggle Logic
    const themeBtn = document.getElementById('theme-toggle');
    if (themeBtn) {
        themeBtn.addEventListener('click', () => {
            document.body.classList.toggle('light-mode');
        });
    }
});
