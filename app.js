// ============================================================
// PCS Academy Quiz Application — BROWSER ONLY
// No require() / No Node.js code. Server lives in server.js
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
            { id:1,  category:'Mathematics',       difficulty:'Easy',   question:'What is 15 + 27?',                                              options:['42','41','43','40'],                                                      correct:0, explanation:'15 + 27 = 42. Add ones (5+7=12, carry 1) then tens (1+2+1=4).' },
            { id:2,  category:'Mathematics',       difficulty:'Easy',   question:'What is the square root of 144?',                               options:['11','12','13','14'],                                                      correct:1, explanation:'sqrt(144) = 12 because 12 x 12 = 144.' },
            { id:3,  category:'Science',           difficulty:'Easy',   question:'What gas do plants absorb during photosynthesis?',               options:['Oxygen','Nitrogen','Carbon Dioxide','Hydrogen'],                          correct:2, explanation:'Plants absorb CO2 and convert it into glucose and oxygen using sunlight.' },
            { id:4,  category:'Science',           difficulty:'Easy',   question:'How many bones are in an adult human body?',                     options:['206','205','207','204'],                                                  correct:0, explanation:'An adult human skeleton has 206 bones.' },
            { id:5,  category:'History',           difficulty:'Easy',   question:'Who was the first President of India?',                          options:['Jawaharlal Nehru','Dr. Rajendra Prasad','Mahatma Gandhi','Sardar Patel'], correct:1, explanation:'Dr. Rajendra Prasad served as India\'s first President from 1950 to 1962.' },
            { id:6,  category:'History',           difficulty:'Easy',   question:'In which year did India gain independence?',                     options:['1945','1946','1947','1948'],                                              correct:2, explanation:'India gained independence from British rule on August 15, 1947.' },
            { id:7,  category:'General Knowledge', difficulty:'Easy',   question:'What is the capital of France?',                                options:['London','Berlin','Paris','Madrid'],                                       correct:2, explanation:'Paris is the capital and largest city of France.' },
            { id:8,  category:'General Knowledge', difficulty:'Easy',   question:'What is the largest mammal in the world?',                      options:['Elephant','Blue Whale','Giraffe','Hippopotamus'],                         correct:1, explanation:'The Blue Whale is the largest animal ever known to have lived on Earth.' },
            { id:9,  category:'Mathematics',       difficulty:'Medium', question:'What is 12 x 15?',                                              options:['180','175','185','170'],                                                  correct:0, explanation:'12 x 15 = 180. Calculate as (12x10)+(12x5) = 120+60.' },
            { id:10, category:'Science',           difficulty:'Medium', question:'What is the chemical symbol for gold?',                         options:['Go','Gd','Au','Ag'],                                                      correct:2, explanation:'Au comes from the Latin word "aurum" meaning gold.' },
            { id:11, category:'Mathematics',       difficulty:'Easy',   question:'What is 100 - 37?',                                             options:['63','62','64','61'],                                                      correct:0, explanation:'100 - 37 = 63.' },
            { id:12, category:'Science',           difficulty:'Easy',   question:'Which planet is known as the Red Planet?',                      options:['Venus','Mars','Jupiter','Saturn'],                                        correct:1, explanation:'Mars looks red due to iron oxide (rust) on its surface.' },
            { id:13, category:'General Knowledge', difficulty:'Easy',   question:'How many continents are there on Earth?',                       options:['5','6','7','8'],                                                          correct:2, explanation:'7 continents: Asia, Africa, North America, South America, Antarctica, Europe, Australia.' },
            { id:14, category:'History',           difficulty:'Medium', question:'Who built the Taj Mahal?',                                      options:['Akbar','Shah Jahan','Humayun','Aurangzeb'],                               correct:1, explanation:'Shah Jahan built the Taj Mahal (~1653) in memory of his wife Mumtaz Mahal.' },
            { id:15, category:'Mathematics',       difficulty:'Medium', question:'What is 25% of 80?',                                            options:['15','20','25','30'],                                                      correct:1, explanation:'25% of 80 = 80 / 4 = 20.' },
            { id:16, category:'English',           difficulty:'Easy',   question:'What is the plural form of "child"?',                           options:['childs','childes','children','childs\''],                                 correct:2, explanation:'"Children" is the irregular plural of "child".' },
            { id:17, category:'English',           difficulty:'Medium', question:'Which word is a synonym for "happy"?',                          options:['Sad','Joyful','Angry','Tired'],                                           correct:1, explanation:'"Joyful" is a synonym for "happy", both express positive emotions.' },
            { id:18, category:'Science',           difficulty:'Medium', question:'What is the process where water changes from liquid to gas?',    options:['Condensation','Evaporation','Precipitation','Sublimation'],               correct:1, explanation:'Evaporation is the liquid-to-gas change driven by heat energy.' },
            { id:19, category:'General Knowledge', difficulty:'Medium', question:'Which is the longest river in the world?',                      options:['Amazon River','Nile River','Mississippi River','Yangtze River'],         correct:1, explanation:'The Nile (~6,650 km) is generally considered the world\'s longest river.' },
            { id:20, category:'History',           difficulty:'Easy',   question:'What year was PCS Academy School established?',                 options:['2020','2021','2022','2023'],                                              correct:2, explanation:'PCS Academy School was established in 2022.' }
        ];

        this.injectStyles();
        this.init();
    }

    // ── Boot ───────────────────────────────────────────────────
    init() {
        var self = this;
        document.querySelectorAll('.particle').forEach(function(p, i) {
            p.style.animationDelay = (i * 0.5) + 's';
        });

        // Show home after 3.5s
        setTimeout(function() {
            self.showScreen('home-screen');
            // Push all AdSense slots 600ms after home is visible
            setTimeout(function() {
                try {
                    document.querySelectorAll('ins.adsbygoogle').forEach(function(ins) {
                        if (!ins.getAttribute('data-adsbygoogle-status')) {
                            (window.adsbygoogle = window.adsbygoogle || []).push({});
                        }
                    });
                } catch(e) { /* AdSense not ready */ }
            }, 600);
        }, 3500);

        this.setupEventListeners();
    }

    // ── Screen switching ───────────────────────────────────────
    showScreen(screenId) {
        var target = document.getElementById(screenId);
        if (!target) { console.error('Screen not found:', screenId); return; }

        document.querySelectorAll('.screen').forEach(function(s) {
            s.classList.remove('active');
            s.style.display = 'none';
        });

        target.classList.add('active');
        target.style.display = (screenId === 'splash-screen') ? 'flex' : 'block';

        this.currentScreen = screenId;
        if (screenId === 'quiz-screen') this.startQuiz();
        window.scrollTo(0, 0);
    }

    // ── Events ─────────────────────────────────────────────────
    setupEventListeners() {
        var self = this;

        document.addEventListener('click', function(e) {
            var btn = e.target.closest('.option-button');
            if (btn && !btn.disabled) self.selectAnswer(btn);
        });

        var submitBtn = document.getElementById('submit-answer');
        var nextBtn   = document.getElementById('next-question');
        if (submitBtn) submitBtn.addEventListener('click', function() { self.submitAnswer(); });
        if (nextBtn)   nextBtn.addEventListener('click',   function() { self.nextQuestion(); });

        document.addEventListener('keydown', function(e) {
            if (self.currentScreen !== 'quiz-screen') return;
            var map = { a:0, b:1, c:2, d:3 };
            var idx = map[e.key.toLowerCase()];
            if (idx !== undefined) {
                self.selectAnswerByIndex(idx);
            } else if ((e.key === 'Enter' || e.key === ' ') && self.selectedAnswer !== null) {
                e.preventDefault();
                self.submitAnswer();
            }
        });

        var form = document.querySelector('.newsletter-form');
        if (form) {
            form.querySelector('.newsletter-btn').addEventListener('click', function() {
                self.handleNewsletterSignup();
            });
        }
    }

    // ── Quiz lifecycle ─────────────────────────────────────────
    startQuiz() {
        this.currentQuestion = 0;
        this.userAnswers     = [];
        this.score           = 0;
        this.selectedAnswer  = null;
        this.quizQuestions   = this.shuffleArray(this.questionDB.slice()).slice(0, this.totalQuestions);

        // Rebuild quiz DOM if results screen replaced it
        var self    = this;
        var wrapper = document.querySelector('.quiz-wrapper');
        if (wrapper && !wrapper.querySelector('.quiz-header')) {
            wrapper.innerHTML =
                '<div class="quiz-header">' +
                '<button onclick="showScreen(\'home-screen\')" class="super-back-btn"><span class="btn-icon">&#8592;</span> Back to Home</button>' +
                '<div class="quiz-progress-info">' +
                '<div class="question-indicator">' +
                '<span id="question-counter" class="question-number">Question 1 of 10</span>' +
                '<div class="progress-bar"><div class="progress-fill" id="progress-fill"></div></div>' +
                '</div>' +
                '<div class="timer-container"><div class="timer-circle">' +
                '<div class="timer-text" id="timer">30</div>' +
                '<svg class="timer-svg" viewBox="0 0 36 36">' +
                '<circle cx="18" cy="18" r="16" fill="none" stroke="#e0f2fe" stroke-width="2"/>' +
                '<circle id="timer-progress" cx="18" cy="18" r="16" fill="none" stroke="#29b6f6" stroke-width="2" stroke-dasharray="100 100" stroke-dashoffset="0"/>' +
                '</svg></div></div>' +
                '</div></div>' +
                '<div class="quiz-content">' +
                '<div class="question-card">' +
                '<div class="question-header">' +
                '<span class="question-category" id="question-category">Mathematics</span>' +
                '<span class="question-difficulty" id="question-difficulty">Easy</span>' +
                '</div>' +
                '<h2 id="question-text" class="question-title">Loading...</h2>' +
                '</div>' +
                '<div class="options-grid" id="options-container"></div>' +
                '<div class="quiz-actions">' +
                '<button id="submit-answer" class="super-btn primary large"><span class="btn-icon">&#10003;</span> Submit Answer</button>' +
                '<button id="next-question" class="super-btn primary large" style="display:none"><span class="btn-icon">&#8594;</span> Next Question</button>' +
                '</div></div>' +
                '<div class="display-ad-container">' +
                '<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-5236839570529719" data-ad-slot="1768612586" data-ad-format="auto" data-full-width-responsive="true"></ins>' +
                '</div>';

            document.getElementById('submit-answer').addEventListener('click', function() { self.submitAnswer(); });
            document.getElementById('next-question').addEventListener('click', function() { self.nextQuestion(); });
        }

        this.displayQuestion();
        this.updateProgressBar();
    }

    displayQuestion() {
        var q = this.quizQuestions[this.currentQuestion];

        var counter = document.getElementById('question-counter');
        if (counter) counter.textContent = 'Question ' + (this.currentQuestion + 1) + ' of ' + this.quizQuestions.length;

        var catEl  = document.getElementById('question-category');
        var diffEl = document.getElementById('question-difficulty');
        if (catEl)  catEl.textContent  = q.category;
        if (diffEl) { diffEl.textContent = q.difficulty; diffEl.className = 'question-difficulty ' + q.difficulty.toLowerCase(); }

        var textEl = document.getElementById('question-text');
        if (textEl) textEl.textContent = q.question;

        var container = document.getElementById('options-container');
        if (container) {
            container.innerHTML = '';
            for (var i = 0; i < q.options.length; i++) {
                var btn = document.createElement('button');
                btn.className     = 'option-button';
                btn.dataset.index = i;
                btn.innerHTML     = '<div class="option-content"><span class="option-letter">' + String.fromCharCode(65 + i) + '</span><span class="option-text">' + q.options[i] + '</span></div>';
                container.appendChild(btn);
            }
        }

        this.selectedAnswer = null;
        var submitBtn = document.getElementById('submit-answer');
        var nextBtn   = document.getElementById('next-question');
        if (submitBtn) submitBtn.style.display = 'inline-flex';
        if (nextBtn)   nextBtn.style.display   = 'none';

        var prev = document.querySelector('.explanation');
        if (prev) prev.remove();

        this.startTimer();
    }

    selectAnswer(btn) {
        document.querySelectorAll('.option-button').forEach(function(o) { o.classList.remove('selected'); });
        btn.classList.add('selected');
        this.selectedAnswer = parseInt(btn.dataset.index);
    }

    selectAnswerByIndex(i) {
        var opts = document.querySelectorAll('.option-button');
        if (opts[i]) this.selectAnswer(opts[i]);
    }

    submitAnswer() {
        if (this.selectedAnswer === null) {
            this.showNotification('Please select an answer before submitting!', 'warning');
            return;
        }
        clearInterval(this.timer);
        var q    = this.quizQuestions[this.currentQuestion];
        var self = this;

        document.querySelectorAll('.option-button').forEach(function(btn, i) {
            btn.disabled = true;
            if (i === q.correct) {
                btn.classList.add('correct');
                self.addIndicator(btn, '&#10003;', 'correct');
            } else if (i === self.selectedAnswer && i !== q.correct) {
                btn.classList.add('incorrect');
                self.addIndicator(btn, '&#10007;', 'incorrect');
            }
        });

        var isCorrect = (this.selectedAnswer === q.correct);
        this.userAnswers.push({ questionId:q.id, question:q.question, selected:this.selectedAnswer, correct:q.correct, isCorrect:isCorrect, category:q.category });

        if (isCorrect) { this.score++; this.showNotification('Correct! Well done! \uD83C\uDF89', 'success'); }
        else           {               this.showNotification('Incorrect. Learn from this! \uD83D\uDCDA', 'error'); }

        this.showExplanation(q.explanation, isCorrect);

        var submitBtn = document.getElementById('submit-answer');
        var nextBtn   = document.getElementById('next-question');
        if (submitBtn) submitBtn.style.display = 'none';
        if (nextBtn)   nextBtn.style.display   = 'inline-flex';
    }

    addIndicator(btn, symbol, type) {
        var el = document.createElement('div');
        el.className = 'answer-indicator ' + type;
        el.innerHTML = symbol;
        btn.appendChild(el);
    }

    showExplanation(text, isCorrect) {
        var div = document.createElement('div');
        div.className = 'explanation ' + (isCorrect ? 'correct' : 'incorrect');
        div.innerHTML =
            '<div class="explanation-header">' +
            '<span class="explanation-icon">' + (isCorrect ? '&#10003;' : '&#10007;') + '</span>' +
            '<span class="explanation-status">' + (isCorrect ? 'Correct!' : 'Incorrect') + '</span>' +
            '</div>' +
            '<div class="explanation-text">' + text + '</div>';
        var card = document.querySelector('.question-card');
        if (card) card.appendChild(div);
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
        var fill = document.getElementById('progress-fill');
        if (fill) fill.style.width = ((this.currentQuestion + 1) / this.quizQuestions.length * 100) + '%';
    }

    // ── Results ────────────────────────────────────────────────
    showResults() {
        clearInterval(this.timer);
        var pct    = Math.round(this.score / this.quizQuestions.length * 100);
        var levels = [
            { min:90, msg:'Outstanding! Exceptional performance!',   emoji:'\uD83C\uDFC6' },
            { min:80, msg:'Excellent work! Great job!',              emoji:'\uD83C\uDF89' },
            { min:70, msg:'Good job! Keep up the good work!',        emoji:'\uD83D\uDC4D' },
            { min:60, msg:'Fair performance. More practice needed.', emoji:'\uD83D\uDCDA' },
            { min:0,  msg:'Keep studying and try again!',            emoji:'\uD83D\uDCAA' }
        ];
        var level = levels.find(function(l) { return pct >= l.min; });
        var stats = this.calculateCategoryStats();

        var statsHTML = stats.map(function(s) {
            return '<div class="category-stat-item">' +
                '<span class="category-name">' + s.category + '</span>' +
                '<div class="category-bar"><div class="category-fill" style="width:' + s.percentage + '%"></div></div>' +
                '<span class="category-percentage">' + s.percentage + '%</span>' +
                '</div>';
        }).join('');

        var wrapper = document.querySelector('.quiz-wrapper');
        if (!wrapper) return;

        wrapper.innerHTML =
            '<div class="results-container">' +
            '<div class="results-header">' +
            '<h1 class="results-title">Quiz Complete! ' + level.emoji + '</h1>' +
            '<div class="results-score-circle"><div class="score-circle-inner">' +
            '<span class="score-percentage">' + pct + '%</span>' +
            '<span class="score-label">Score</span>' +
            '</div></div></div>' +
            '<div class="results-summary">' +
            '<div class="summary-item"><span class="summary-number">' + this.score + '</span><span class="summary-label">Correct</span></div>' +
            '<div class="summary-item"><span class="summary-number">' + (this.quizQuestions.length - this.score) + '</span><span class="summary-label">Incorrect</span></div>' +
            '<div class="summary-item"><span class="summary-number">' + this.quizQuestions.length + '</span><span class="summary-label">Total</span></div>' +
            '</div>' +
            '<div class="results-message"><h3>' + level.msg + '</h3></div>' +
            '<div class="category-performance"><h3>Performance by Category</h3>' +
            '<div class="category-stats">' + statsHTML + '</div></div>' +
            '<div class="results-actions">' +
            '<button onclick="quizApp.startQuiz()" class="super-btn primary large"><span class="btn-icon">\uD83D\uDD04</span> Take Quiz Again</button>' +
            '<button onclick="quizApp.showScreen(\'home-screen\')" class="super-btn secondary large"><span class="btn-icon">\uD83C\uDFE0</span> Back to Home</button>' +
            '</div>' +
            '<div class="display-ad-container">' +
            '<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-5236839570529719" data-ad-slot="1768612586" data-ad-format="auto" data-full-width-responsive="true"></ins>' +
            '</div></div>';

        // Push ad for newly created slot
        try {
            (window.adsbygoogle = window.adsbygoogle || []).push({});
        } catch(e) {}
    }

    calculateCategoryStats() {
        var cats = {};
        this.userAnswers.forEach(function(a) {
            if (!cats[a.category]) cats[a.category] = { correct:0, total:0 };
            cats[a.category].total++;
            if (a.isCorrect) cats[a.category].correct++;
        });
        return Object.keys(cats).map(function(c) {
            return { category:c, correct:cats[c].correct, total:cats[c].total, percentage:Math.round(cats[c].correct / cats[c].total * 100) };
        });
    }

    // ── Timer ──────────────────────────────────────────────────
    startTimer() {
        clearInterval(this.timer);
        this.timeLeft = 30;
        var self      = this;

        this.timer = setInterval(function() {
            self.timeLeft--;
            var timerText = document.getElementById('timer');
            var timerProg = document.getElementById('timer-progress');
            if (timerText) timerText.textContent = self.timeLeft;
            if (timerProg) timerProg.style.strokeDashoffset = (100 - self.timeLeft / 30 * 100).toString();

            var color = self.timeLeft <= 5 ? '#f44336' : self.timeLeft <= 10 ? '#ff9800' : '#29b6f6';
            if (timerText) timerText.style.color = color;
            if (timerProg) timerProg.style.stroke  = color;

            if (self.timeLeft <= 0) {
                clearInterval(self.timer);
                if (self.selectedAnswer === null) {
                    self.showNotification("Time's up! Moving to next question.", 'warning');
                    self.nextQuestion();
                } else {
                    self.submitAnswer();
                }
            }
        }, 1000);
    }

    // ── Notification ───────────────────────────────────────────
    showNotification(message, type) {
        document.querySelectorAll('.pcs-notif').forEach(function(n) { n.remove(); });
        var n = document.createElement('div');
        n.className = 'pcs-notif pcs-notif-' + (type || 'info');
        n.innerHTML = '<span>' + message + '</span><button onclick="this.parentElement.remove()">&#215;</button>';
        document.body.appendChild(n);
        setTimeout(function() {
            if (n.parentElement) { n.style.opacity = '0'; setTimeout(function() { n.remove(); }, 300); }
        }, 4000);
    }

    // ── Newsletter ─────────────────────────────────────────────
    handleNewsletterSignup() {
        var input = document.querySelector('.newsletter-input');
        var email = input ? input.value.trim() : '';
        if (email && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
            this.showNotification('Thank you for subscribing!', 'success');
            if (input) input.value = '';
        } else {
            this.showNotification('Please enter a valid email address.', 'error');
        }
    }

    // ── Helpers ────────────────────────────────────────────────
    shuffleArray(arr) {
        for (var i = arr.length - 1; i > 0; i--) {
            var j   = Math.floor(Math.random() * (i + 1));
            var tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
        }
        return arr;
    }

    // ── Injected styles ────────────────────────────────────────
    injectStyles() {
        if (document.getElementById('pcs-dyn')) return;
        var s = document.createElement('style');
        s.id  = 'pcs-dyn';
        s.textContent =
            '@keyframes btnRipple { to { transform:scale(2.5);opacity:0; } }' +
            '@keyframes slideInRight { from { transform:translateX(110%);opacity:0; } to { transform:translateX(0);opacity:1; } }' +
            '.pcs-notif { position:fixed;top:20px;right:20px;z-index:10000;display:flex;align-items:center;gap:1rem;max-width:380px;padding:.85rem 1.1rem;border-radius:12px;box-shadow:0 8px 24px rgba(0,0,0,.18);animation:slideInRight .3s ease-out;transition:opacity .3s;font-size:.95rem;font-weight:500; }' +
            '.pcs-notif button { background:none;border:none;color:inherit;font-size:1.3rem;cursor:pointer;opacity:.7;margin-left:auto; }' +
            '.pcs-notif-success { background:#4caf50;color:#fff; }' +
            '.pcs-notif-error   { background:#f44336;color:#fff; }' +
            '.pcs-notif-warning { background:#ff9800;color:#fff; }' +
            '.pcs-notif-info    { background:#29b6f6;color:#fff; }' +
            '.option-content { display:flex;align-items:center;gap:1rem; }' +
            '.option-letter { display:flex;align-items:center;justify-content:center;width:32px;height:32px;min-width:32px;background:rgba(41,182,246,.12);color:#29b6f6;border-radius:50%;font-weight:700;font-size:.9rem;transition:.15s; }' +
            '.option-button.selected .option-letter,.option-button.correct .option-letter,.option-button.incorrect .option-letter { background:rgba(255,255,255,.25);color:#fff; }' +
            '.option-text { flex:1; }' +
            '.answer-indicator { position:absolute;right:1rem;top:50%;transform:translateY(-50%);width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:1rem;background:rgba(255,255,255,.3);color:#fff; }' +
            '.explanation { margin-top:1.5rem;padding:1.25rem 1.5rem;border-radius:12px;border-left:4px solid; }' +
            '.explanation.correct   { background:#e8f5e9;border-color:#4caf50; }' +
            '.explanation.incorrect { background:#ffebee;border-color:#f44336; }' +
            '.explanation-header { display:flex;align-items:center;gap:.5rem;font-weight:700;margin-bottom:.5rem;font-size:1.05rem; }' +
            '.explanation.correct   .explanation-header { color:#2e7d32; }' +
            '.explanation.incorrect .explanation-header { color:#c62828; }' +
            '.explanation-text { color:#555;line-height:1.6;font-size:.95rem; }' +
            '.question-difficulty.easy   { background:#e8f5e9;color:#2e7d32; }' +
            '.question-difficulty.medium { background:#fff3e0;color:#e65100; }' +
            '.question-difficulty.hard   { background:#ffebee;color:#c62828; }' +
            '.results-container { max-width:600px;margin:2rem auto;padding:2rem;text-align:center;background:#fff;border-radius:20px;box-shadow:0 20px 40px rgba(41,182,246,.15);border:1px solid #e0f2fe; }' +
            '.results-title { font-size:2rem;color:#29b6f6;margin-bottom:1.5rem; }' +
            '.results-score-circle { width:150px;height:150px;margin:0 auto 1.5rem;border-radius:50%;background:linear-gradient(135deg,#29b6f6,#0288d1);display:flex;align-items:center;justify-content:center;box-shadow:0 10px 30px rgba(41,182,246,.35); }' +
            '.score-circle-inner { color:#fff;text-align:center; }' +
            '.score-percentage { display:block;font-size:2.5rem;font-weight:800; }' +
            '.score-label { font-size:.9rem;opacity:.9;text-transform:uppercase;letter-spacing:.06em; }' +
            '.results-summary { display:flex;justify-content:space-around;margin:1.5rem 0;padding:1.4rem;background:#f0f9ff;border-radius:14px; }' +
            '.summary-number { display:block;font-size:1.8rem;font-weight:700;color:#29b6f6; }' +
            '.summary-label { font-size:.85rem;color:#666;text-transform:uppercase; }' +
            '.results-message { margin:1.5rem 0;padding:1rem 1.25rem;border-left:4px solid #29b6f6;border-radius:0 10px 10px 0;background:#f9feff;text-align:left; }' +
            '.results-message h3 { color:#29b6f6;margin:0; }' +
            '.category-performance { margin:1.5rem 0;text-align:left; }' +
            '.category-performance > h3 { text-align:center;color:#29b6f6;margin-bottom:1rem; }' +
            '.category-stats { display:flex;flex-direction:column;gap:.8rem; }' +
            '.category-stat-item { display:flex;align-items:center;gap:.75rem; }' +
            '.category-name { min-width:130px;font-weight:600;font-size:.88rem; }' +
            '.category-bar { flex:1;height:8px;background:#e0e0e0;border-radius:4px;overflow:hidden; }' +
            '.category-fill { height:100%;background:#29b6f6;transition:width 1s ease-in-out; }' +
            '.category-percentage { min-width:42px;text-align:right;font-weight:600;color:#29b6f6;font-size:.88rem; }' +
            '.results-actions { display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;margin-top:2rem; }';
        document.head.appendChild(s);
    }
}

// ── Global helpers ────────────────────────────────────────────
function showScreen(screenId) {
    if (window.quizApp) window.quizApp.showScreen(screenId);
}

// ── Contact Form (no mailto: form action — avoids Mixed Content) ──
function handleContactForm(e) {
    e.preventDefault();
    var name    = (document.getElementById('name')    || {}).value || '';
    var email   = (document.getElementById('email')   || {}).value || '';
    var subject = (document.getElementById('subject') || {}).value || '';
    var message = (document.getElementById('message') || {}).value || '';

    if (!name || !email || !subject || !message) {
        if (window.quizApp) window.quizApp.showNotification('Please fill in all fields.', 'warning');
        return;
    }
    var body = encodeURIComponent('Name: ' + name + '\nEmail: ' + email + '\n\n' + message);
    var sub  = encodeURIComponent(subject + ' — ' + name);
    window.location.href = 'mailto:pcsacademyschool@gmail.com?subject=' + sub + '&body=' + body;
    if (window.quizApp) window.quizApp.showNotification('Opening your email client...', 'success');
    document.getElementById('contact-form').reset();
}

// ── Boot ──────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', function() {
    window.quizApp = new PCSQuizApp();

    // Card hover lift
    document.querySelectorAll('.feature-card, .contact-method').forEach(function(card) {
        card.addEventListener('mouseenter', function() { card.style.transform = 'translateY(-5px)'; });
        card.addEventListener('mouseleave', function() { card.style.transform = ''; });
    });

    // Button ripple effect
    document.addEventListener('click', function(e) {
        var btn = e.target.closest('.super-btn, .option-button');
        if (!btn) return;
        var r    = document.createElement('div');
        var rect = btn.getBoundingClientRect();
        var size = Math.max(rect.width, rect.height);
        r.style.cssText =
            'position:absolute;border-radius:50%;pointer-events:none;' +
            'width:' + size + 'px;height:' + size + 'px;' +
            'left:' + (e.clientX - rect.left - size / 2) + 'px;' +
            'top:'  + (e.clientY - rect.top  - size / 2) + 'px;' +
            'background:rgba(255,255,255,.3);transform:scale(0);animation:btnRipple .6s linear;';
        btn.style.position = 'relative';
        btn.style.overflow = 'hidden';
        btn.appendChild(r);
        setTimeout(function() { r.remove(); }, 600);
    });
});

window.PCSQuizApp = PCSQuizApp;
