// ============================================================
// PCS Academy Quiz Application
// ⚠️  BROWSER-ONLY FILE — no require(), no Node.js code here
//     Server code lives entirely in server.js
// ============================================================

class PCSQuizApp {
    constructor() {
        this.currentScreen   = 'splash-screen';
        this.currentQuestion = 0;
        this.quizQuestions   = [];
        this.userAnswers     = [];
        this.score           = 0;
        this.timer           = null;
        this.timeLeft        = 30;
        this.selectedAnswer  = null;
        this.totalQuestions  = 10;

        this.questionDB = [
            { id:1,  category:"Mathematics",       difficulty:"Easy",   question:"What is 15 + 27?",                                              options:["42","41","43","40"],                                                      correct:0, explanation:"15 + 27 = 42. Add ones (5+7=12, carry 1) then tens (1+2+1=4)." },
            { id:2,  category:"Mathematics",       difficulty:"Easy",   question:"What is the square root of 144?",                               options:["11","12","13","14"],                                                      correct:1, explanation:"√144 = 12 because 12 × 12 = 144." },
            { id:3,  category:"Science",           difficulty:"Easy",   question:"What gas do plants absorb during photosynthesis?",               options:["Oxygen","Nitrogen","Carbon Dioxide","Hydrogen"],                          correct:2, explanation:"Plants absorb CO₂ and convert it into glucose and oxygen using sunlight." },
            { id:4,  category:"Science",           difficulty:"Easy",   question:"How many bones are in an adult human body?",                     options:["206","205","207","204"],                                                  correct:0, explanation:"An adult human skeleton has 206 bones." },
            { id:5,  category:"History",           difficulty:"Easy",   question:"Who was the first President of India?",                          options:["Jawaharlal Nehru","Dr. Rajendra Prasad","Mahatma Gandhi","Sardar Patel"], correct:1, explanation:"Dr. Rajendra Prasad served as India's first President from 1950 to 1962." },
            { id:6,  category:"History",           difficulty:"Easy",   question:"In which year did India gain independence?",                     options:["1945","1946","1947","1948"],                                              correct:2, explanation:"India gained independence from British rule on August 15, 1947." },
            { id:7,  category:"General Knowledge", difficulty:"Easy",   question:"What is the capital of France?",                                options:["London","Berlin","Paris","Madrid"],                                       correct:2, explanation:"Paris is the capital and largest city of France." },
            { id:8,  category:"General Knowledge", difficulty:"Easy",   question:"What is the largest mammal in the world?",                      options:["Elephant","Blue Whale","Giraffe","Hippopotamus"],                         correct:1, explanation:"The Blue Whale is the largest animal ever known to have lived on Earth." },
            { id:9,  category:"Mathematics",       difficulty:"Medium", question:"What is 12 × 15?",                                              options:["180","175","185","170"],                                                  correct:0, explanation:"12 × 15 = 180. Calculate as (12×10)+(12×5) = 120+60." },
            { id:10, category:"Science",           difficulty:"Medium", question:"What is the chemical symbol for gold?",                         options:["Go","Gd","Au","Ag"],                                                      correct:2, explanation:"Au comes from the Latin word 'aurum' meaning gold." },
            { id:11, category:"Mathematics",       difficulty:"Easy",   question:"What is 100 - 37?",                                             options:["63","62","64","61"],                                                      correct:0, explanation:"100 - 37 = 63." },
            { id:12, category:"Science",           difficulty:"Easy",   question:"Which planet is known as the Red Planet?",                      options:["Venus","Mars","Jupiter","Saturn"],                                        correct:1, explanation:"Mars looks red due to iron oxide (rust) covering its surface." },
            { id:13, category:"General Knowledge", difficulty:"Easy",   question:"How many continents are there on Earth?",                       options:["5","6","7","8"],                                                          correct:2, explanation:"7 continents: Asia, Africa, North America, South America, Antarctica, Europe, Australia." },
            { id:14, category:"History",           difficulty:"Medium", question:"Who built the Taj Mahal?",                                      options:["Akbar","Shah Jahan","Humayun","Aurangzeb"],                               correct:1, explanation:"Shah Jahan built the Taj Mahal (~1653) in memory of his wife Mumtaz Mahal." },
            { id:15, category:"Mathematics",       difficulty:"Medium", question:"What is 25% of 80?",                                            options:["15","20","25","30"],                                                      correct:1, explanation:"25% of 80 = 80 ÷ 4 = 20." },
            { id:16, category:"English",           difficulty:"Easy",   question:"What is the plural form of 'child'?",                           options:["childs","childes","children","childs'"],                                  correct:2, explanation:"'Children' is the irregular plural of 'child'." },
            { id:17, category:"English",           difficulty:"Medium", question:"Which word is a synonym for 'happy'?",                          options:["Sad","Joyful","Angry","Tired"],                                           correct:1, explanation:"'Joyful' is a synonym for 'happy' — both express positive emotions." },
            { id:18, category:"Science",           difficulty:"Medium", question:"What is the process where water changes from liquid to gas?",    options:["Condensation","Evaporation","Precipitation","Sublimation"],               correct:1, explanation:"Evaporation is the liquid-to-gas change driven by heat energy." },
            { id:19, category:"General Knowledge", difficulty:"Medium", question:"Which is the longest river in the world?",                      options:["Amazon River","Nile River","Mississippi River","Yangtze River"],         correct:1, explanation:"The Nile (~6,650 km) is generally considered the world's longest river." },
            { id:20, category:"History",           difficulty:"Easy",   question:"What year was PCS Academy School established?",                 options:["2020","2021","2022","2023"],                                              correct:2, explanation:"PCS Academy School was established in 2022." }
        ];

        this.injectStyles();
        this.init();
    }

    // ── Boot ───────────────────────────────────────────────────
    init() {
        this.animateSplashParticles();
        setTimeout(() => this.showScreen('home-screen'), 4000);
        this.setupEventListeners();
    }

    animateSplashParticles() {
        document.querySelectorAll('.particle').forEach((p, i) => {
            p.style.animationDelay = `${i * 0.5}s`;
        });
    }

    // ── Event listeners ────────────────────────────────────────
    setupEventListeners() {
        // Answer selection (event delegation)
        document.addEventListener('click', (e) => {
            const btn = e.target.closest('.option-button');
            if (btn && !btn.disabled) this.selectAnswer(btn);
        });

        document.getElementById('submit-answer')
            ?.addEventListener('click', () => this.submitAnswer());
        document.getElementById('next-question')
            ?.addEventListener('click', () => this.nextQuestion());

        // Keyboard shortcuts A/B/C/D + Enter/Space
        document.addEventListener('keydown', (e) => {
            if (this.currentScreen !== 'quiz-screen') return;
            const keyMap = { a:0, b:1, c:2, d:3 };
            if (keyMap[e.key.toLowerCase()] !== undefined) {
                this.selectAnswerByIndex(keyMap[e.key.toLowerCase()]);
            } else if ((e.key === 'Enter' || e.key === ' ') && this.selectedAnswer !== null) {
                e.preventDefault();
                this.submitAnswer();
            }
        });

        // Newsletter
        document.querySelector('.newsletter-form')
            ?.addEventListener('submit', (e) => { e.preventDefault(); this.handleNewsletterSignup(); });
    }

    // ── Screen navigation ──────────────────────────────────────
    showScreen(screenId) {
        const current = document.querySelector('.screen.active');
        const target  = document.getElementById(screenId);
        if (!target) return;

        const activate = () => {
            target.classList.add('active');
            requestAnimationFrame(() => {
                target.style.opacity   = '1';
                target.style.transform = 'translateY(0)';
            });
            this.currentScreen = screenId;
            if (screenId === 'quiz-screen') this.startQuiz();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        };

        if (current && current !== target) {
            current.style.opacity   = '0';
            current.style.transform = 'translateY(-20px)';
            setTimeout(() => { current.classList.remove('active'); activate(); }, 300);
        } else {
            activate();
        }
    }

    // ── Quiz lifecycle ─────────────────────────────────────────
    startQuiz() {
        this.currentQuestion = 0;
        this.userAnswers     = [];
        this.score           = 0;
        this.selectedAnswer  = null;
        this.quizQuestions   = this.shuffleArray([...this.questionDB]).slice(0, this.totalQuestions);
        this.displayQuestion();
        this.updateProgressBar();
    }

    displayQuestion() {
        const q = this.quizQuestions[this.currentQuestion];

        // Header info
        const counterEl = document.getElementById('question-counter');
        if (counterEl) counterEl.textContent = `Question ${this.currentQuestion + 1} of ${this.quizQuestions.length}`;

        const catEl  = document.getElementById('question-category');
        const diffEl = document.getElementById('question-difficulty');
        if (catEl)  catEl.textContent  = q.category;
        if (diffEl) { diffEl.textContent = q.difficulty; diffEl.className = `question-difficulty ${q.difficulty.toLowerCase()}`; }

        // Question text
        const textEl = document.getElementById('question-text');
        if (textEl) textEl.textContent = q.question;

        // Answer options
        const container = document.getElementById('options-container');
        if (container) {
            container.innerHTML = '';
            q.options.forEach((opt, i) => {
                const btn = document.createElement('button');
                btn.className     = 'option-button';
                btn.dataset.index = i;
                btn.innerHTML     = `
                    <div class="option-content">
                        <span class="option-letter">${String.fromCharCode(65 + i)}</span>
                        <span class="option-text">${opt}</span>
                    </div>`;
                container.appendChild(btn);
            });
        }

        // Reset state
        this.selectedAnswer = null;
        const submitBtn = document.getElementById('submit-answer');
        const nextBtn   = document.getElementById('next-question');
        if (submitBtn) submitBtn.style.display = 'inline-flex';
        if (nextBtn)   nextBtn.style.display   = 'none';

        // Remove old explanation
        document.querySelector('.explanation')?.remove();

        // Start countdown
        this.startTimer();
    }

    // ── Answer handling ────────────────────────────────────────
    selectAnswer(btn) {
        document.querySelectorAll('.option-button').forEach(o => o.classList.remove('selected'));
        btn.classList.add('selected');
        this.selectedAnswer = parseInt(btn.dataset.index);
        btn.style.transform = 'scale(1.02)';
        setTimeout(() => { btn.style.transform = ''; }, 150);
    }

    selectAnswerByIndex(i) {
        const opts = document.querySelectorAll('.option-button');
        if (opts[i]) this.selectAnswer(opts[i]);
    }

    submitAnswer() {
        if (this.selectedAnswer === null) {
            this.showNotification('Please select an answer before submitting!', 'warning');
            return;
        }

        clearInterval(this.timer);
        const q = this.quizQuestions[this.currentQuestion];

        // Mark answers
        document.querySelectorAll('.option-button').forEach((btn, i) => {
            btn.disabled = true;
            if (i === q.correct) {
                btn.classList.add('correct');
                this.addIndicator(btn, '✓', 'correct');
            } else if (i === this.selectedAnswer && i !== q.correct) {
                btn.classList.add('incorrect');
                this.addIndicator(btn, '✗', 'incorrect');
            }
        });

        const isCorrect = this.selectedAnswer === q.correct;
        this.userAnswers.push({
            questionId: q.id, question: q.question,
            selected: this.selectedAnswer, correct: q.correct,
            isCorrect, category: q.category
        });

        if (isCorrect) { this.score++; this.showNotification('Correct! Well done! 🎉', 'success'); }
        else           {               this.showNotification('Incorrect. Learn from this! 📚', 'error'); }

        this.showExplanation(q.explanation, isCorrect);

        document.getElementById('submit-answer').style.display = 'none';
        document.getElementById('next-question').style.display = 'inline-flex';
    }

    addIndicator(btn, symbol, type) {
        const el = document.createElement('div');
        el.className   = `answer-indicator ${type}`;
        el.textContent = symbol;
        btn.appendChild(el);
    }

    showExplanation(text, isCorrect) {
        const div = document.createElement('div');
        div.className = `explanation ${isCorrect ? 'correct' : 'incorrect'}`;
        div.style.opacity   = '0';
        div.style.transform = 'translateY(10px)';
        div.style.transition = 'opacity .3s, transform .3s';
        div.innerHTML = `
            <div class="explanation-header">
                <span class="explanation-icon">${isCorrect ? '✓' : '✗'}</span>
                <span class="explanation-status">${isCorrect ? 'Correct!' : 'Incorrect'}</span>
            </div>
            <div class="explanation-text">${text}</div>`;
        document.querySelector('.question-card')?.appendChild(div);
        requestAnimationFrame(() => { div.style.opacity = '1'; div.style.transform = 'translateY(0)'; });
    }

    nextQuestion() {
        this.currentQuestion++;
        if (this.currentQuestion < this.quizQuestions.length) {
            this.displayQuestion();
            this.updateProgressBar();
        } else {
            this.showResults();
        }
    }

    updateProgressBar() {
        const fill = document.getElementById('progress-fill');
        if (fill) fill.style.width = `${((this.currentQuestion + 1) / this.quizQuestions.length) * 100}%`;
    }

    // ── Results ────────────────────────────────────────────────
    showResults() {
        const pct    = Math.round((this.score / this.quizQuestions.length) * 100);
        const levels = [
            { min:90, msg:'Outstanding! Exceptional performance!',  emoji:'🏆' },
            { min:80, msg:'Excellent work! Great job!',             emoji:'🎉' },
            { min:70, msg:'Good job! Keep up the good work!',       emoji:'👍' },
            { min:60, msg:'Fair performance. More practice needed.', emoji:'📚' },
            { min:0,  msg:'Keep studying and try again!',           emoji:'💪' }
        ];
        const { msg, emoji } = levels.find(l => pct >= l.min);
        const stats = this.calculateCategoryStats();

        const wrapper = document.querySelector('.quiz-wrapper');
        if (!wrapper) return;

        wrapper.innerHTML = `
            <div class="results-container">
                <div class="results-header">
                    <h1 class="results-title">Quiz Complete! ${emoji}</h1>
                    <div class="results-score-circle">
                        <div class="score-circle-inner">
                            <span class="score-percentage">${pct}%</span>
                            <span class="score-label">Score</span>
                        </div>
                    </div>
                </div>

                <div class="results-summary">
                    <div class="summary-item">
                        <span class="summary-number">${this.score}</span>
                        <span class="summary-label">Correct</span>
                    </div>
                    <div class="summary-item">
                        <span class="summary-number">${this.quizQuestions.length - this.score}</span>
                        <span class="summary-label">Incorrect</span>
                    </div>
                    <div class="summary-item">
                        <span class="summary-number">${this.quizQuestions.length}</span>
                        <span class="summary-label">Total</span>
                    </div>
                </div>

                <div class="results-message"><h3>${msg}</h3></div>

                <div class="category-performance">
                    <h3>Performance by Category</h3>
                    <div class="category-stats">
                        ${stats.map(s => `
                            <div class="category-stat-item">
                                <span class="category-name">${s.category}</span>
                                <div class="category-bar">
                                    <div class="category-fill" style="width:${s.percentage}%"></div>
                                </div>
                                <span class="category-percentage">${s.percentage}%</span>
                            </div>`).join('')}
                    </div>
                </div>

                <div class="results-actions">
                    <button onclick="quizApp.startQuiz()" class="super-btn primary large">
                        <span class="btn-icon">🔄</span> Take Quiz Again
                    </button>
                    <button onclick="quizApp.showScreen('home-screen')" class="super-btn secondary large">
                        <span class="btn-icon">🏠</span> Back to Home
                    </button>
                </div>
            </div>`;
    }

    calculateCategoryStats() {
        const cats = {};
        this.userAnswers.forEach(({ category, isCorrect }) => {
            if (!cats[category]) cats[category] = { correct:0, total:0 };
            cats[category].total++;
            if (isCorrect) cats[category].correct++;
        });
        return Object.entries(cats).map(([category, { correct, total }]) => ({
            category, correct, total,
            percentage: Math.round((correct / total) * 100)
        }));
    }

    // ── Timer ──────────────────────────────────────────────────
    startTimer() {
        clearInterval(this.timer);
        this.timeLeft = 30;

        const timerText = document.getElementById('timer');
        const timerProg = document.getElementById('timer-progress');

        this.timer = setInterval(() => {
            this.timeLeft--;

            if (timerText) timerText.textContent = this.timeLeft;
            if (timerProg) timerProg.style.strokeDashoffset = 100 - (this.timeLeft / 30) * 100;

            const color = this.timeLeft <= 5 ? '#f44336' : this.timeLeft <= 10 ? '#ff9800' : '#29b6f6';
            if (timerText) timerText.style.color  = color;
            if (timerProg) timerProg.style.stroke  = color;

            if (this.timeLeft <= 0) {
                clearInterval(this.timer);
                if (this.selectedAnswer === null) {
                    this.showNotification("Time's up! Moving to next question.", 'warning');
                    this.nextQuestion();
                } else {
                    this.submitAnswer();
                }
            }
        }, 1000);
    }

    // ── Notifications ──────────────────────────────────────────
    showNotification(message, type = 'info') {
        document.querySelectorAll('.notification').forEach(n => n.remove());
        const n = document.createElement('div');
        n.className = `notification notification-${type}`;
        n.innerHTML = `
            <div class="notification-content">
                <span>${message}</span>
                <button onclick="this.closest('.notification').remove()">×</button>
            </div>`;
        document.body.appendChild(n);
        setTimeout(() => {
            if (n.parentElement) { n.style.opacity = '0'; setTimeout(() => n.remove(), 300); }
        }, 5000);
    }

    // ── Newsletter ─────────────────────────────────────────────
    handleNewsletterSignup() {
        const input = document.querySelector('.newsletter-input');
        const email = input?.value.trim() ?? '';
        if (email && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
            this.showNotification('Thank you for subscribing! 📧', 'success');
            if (input) input.value = '';
        } else {
            this.showNotification('Please enter a valid email address.', 'error');
        }
    }

    // ── Helpers ────────────────────────────────────────────────
    shuffleArray(arr) {
        for (let i = arr.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
        return arr;
    }

    // ── Inject all dynamic CSS once ────────────────────────────
    injectStyles() {
        if (document.getElementById('pcs-quiz-styles')) return;
        const s = document.createElement('style');
        s.id = 'pcs-quiz-styles';
        s.textContent = `
            /* ── Animations ── */
            @keyframes buttonRipple { to { transform:scale(2); opacity:0; } }
            @keyframes slideInRight { from { transform:translateX(110%); opacity:0; } to { transform:translateX(0); opacity:1; } }

            /* ── Notifications ── */
            .notification {
                position:fixed; top:20px; right:20px; z-index:10000;
                max-width:380px; padding:.9rem 1.1rem; border-radius:12px;
                box-shadow:0 8px 24px rgba(0,0,0,.18);
                animation:slideInRight .3s ease-out;
                transition:opacity .3s;
            }
            .notification-success { background:#4caf50; color:#fff; }
            .notification-error   { background:#f44336; color:#fff; }
            .notification-warning { background:#ff9800; color:#fff; }
            .notification-info    { background:#29b6f6; color:#fff; }
            .notification-content { display:flex; align-items:center; justify-content:space-between; gap:.8rem; }
            .notification-content button { background:none; border:none; color:inherit; font-size:1.4rem; line-height:1; cursor:pointer; opacity:.75; }
            .notification-content button:hover { opacity:1; }

            /* ── Results ── */
            .results-container { max-width:600px; margin:0 auto; padding:2rem; text-align:center; background:#fff; border-radius:20px; box-shadow:0 20px 40px rgba(41,182,246,.15); }
            .results-title { font-size:2rem; color:var(--primary,#29b6f6); margin-bottom:1.5rem; }
            .results-score-circle { width:150px; height:150px; margin:0 auto; border-radius:50%; background:linear-gradient(135deg,var(--primary,#29b6f6),#0288d1); display:flex; align-items:center; justify-content:center; box-shadow:0 10px 30px rgba(41,182,246,.3); }
            .score-circle-inner   { color:#fff; text-align:center; }
            .score-percentage     { display:block; font-size:2.5rem; font-weight:800; }
            .score-label          { font-size:.95rem; opacity:.9; text-transform:uppercase; letter-spacing:.06em; }
            .results-summary      { display:flex; justify-content:space-around; margin:2rem 0; padding:1.4rem; background:#f0f9ff; border-radius:14px; }
            .summary-number       { display:block; font-size:1.8rem; font-weight:700; color:var(--primary,#29b6f6); }
            .summary-label        { font-size:.85rem; color:#666; text-transform:uppercase; letter-spacing:.04em; }
            .results-message      { margin:1.5rem 0; padding:1rem 1.2rem; border-left:4px solid var(--primary,#29b6f6); border-radius:0 10px 10px 0; background:#fafeff; }
            .results-message h3   { color:var(--primary,#29b6f6); margin:0; }
            .category-performance          { margin:1.5rem 0; text-align:left; }
            .category-performance > h3     { text-align:center; color:var(--primary,#29b6f6); margin-bottom:1rem; }
            .category-stats                { display:flex; flex-direction:column; gap:.85rem; }
            .category-stat-item            { display:flex; align-items:center; gap:.8rem; }
            .category-name                 { min-width:130px; font-weight:600; font-size:.88rem; }
            .category-bar                  { flex:1; height:8px; background:#e0e0e0; border-radius:4px; overflow:hidden; }
            .category-fill                 { height:100%; background:var(--primary,#29b6f6); transition:width 1s ease-in-out; }
            .category-percentage           { min-width:42px; text-align:right; font-weight:600; color:var(--primary,#29b6f6); font-size:.88rem; }
            .results-actions               { display:flex; gap:1rem; justify-content:center; flex-wrap:wrap; margin-top:2rem; }
        `;
        document.head.appendChild(s);
    }
}

// ── Global helper called by HTML onclick attributes ─────────
function showScreen(screenId) {
    window.quizApp?.showScreen(screenId);
}

// ── Boot on DOMContentLoaded ────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
    window.quizApp = new PCSQuizApp();

    // Smooth scroll for anchor links
    document.addEventListener('click', (e) => {
        const a = e.target.closest('a[href^="#"]');
        if (a) {
            e.preventDefault();
            document.querySelector(a.getAttribute('href'))
                ?.scrollIntoView({ behavior:'smooth', block:'start' });
        }
    });

    // Mark body as fully loaded
    window.addEventListener('load', () => document.body.classList.add('loaded'));

    // Lazy-load images with data-src
    if ('IntersectionObserver' in window) {
        const io = new IntersectionObserver((entries, obs) => {
            entries.forEach(({ isIntersecting, target }) => {
                if (isIntersecting && target.dataset.src) {
                    target.src = target.dataset.src;
                    target.removeAttribute('data-src');
                    obs.unobserve(target);
                }
            });
        });
        document.querySelectorAll('img[data-src]').forEach(img => io.observe(img));
    }

    // Card hover-lift
    document.querySelectorAll('.feature-card, .question-card, .contact-method').forEach(card => {
        card.addEventListener('mouseenter', () => { card.style.transform = 'translateY(-5px)'; });
        card.addEventListener('mouseleave', () => { card.style.transform = 'translateY(0)'; });
    });

    // Button ripple
    document.querySelectorAll('.super-btn, .option-button').forEach(btn => {
        btn.addEventListener('click', function (e) {
            const r    = document.createElement('div');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            r.style.cssText = `
                position:absolute; border-radius:50%; pointer-events:none;
                width:${size}px; height:${size}px;
                left:${e.clientX - rect.left - size/2}px;
                top:${e.clientY - rect.top  - size/2}px;
                background:rgba(255,255,255,.3);
                transform:scale(0); animation:buttonRipple .6s linear;`;
            this.style.position = 'relative';
            this.style.overflow = 'hidden';
            this.appendChild(r);
            setTimeout(() => r.remove(), 600);
        });
    });
});

window.PCSQuizApp = PCSQuizApp;
