// ============================================================
// PCS Academy Quiz Application — MASTER ENGINE v42.0
// Features: Dark Mode, LocalStorage Tracking, 42 Questions, 
// Confetti Animation API, and Safe AdSense Hooks.
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
        this.totalQuestions  = 10; // Serves 10 questions per run
        this.isDarkMode      = false;
        
        // Local Storage Tracking
        this.totalLifetimeScore = parseInt(localStorage.getItem('pcs_quixler_score')) || 0;

        // Massive 42-Question Database
        this.questionDB = [
            { id:1, category:'Mathematics', difficulty:'Easy', question:'What is 15 + 27?', options:['42','41','43','40'], correct:0, explanation:'15 + 27 = 42.' },
            { id:2, category:'Mathematics', difficulty:'Easy', question:'Square root of 144?', options:['11','12','13','14'], correct:1, explanation:'12 x 12 = 144.' },
            { id:3, category:'Science', difficulty:'Easy', question:'Gas plants absorb?', options:['Oxygen','Nitrogen','Carbon Dioxide','Hydrogen'], correct:2, explanation:'Plants absorb CO2.' },
            { id:4, category:'Science', difficulty:'Easy', question:'Bones in adult body?', options:['206','205','207','204'], correct:0, explanation:'Adults have 206 bones.' },
            { id:5, category:'History', difficulty:'Easy', question:'First President of India?', options:['Nehru','Rajendra Prasad','Gandhi','Patel'], correct:1, explanation:'Dr. Rajendra Prasad.' },
            { id:6, category:'History', difficulty:'Easy', question:'Year of Indian independence?', options:['1945','1946','1947','1948'], correct:2, explanation:'August 15, 1947.' },
            { id:7, category:'General Knowledge', difficulty:'Easy', question:'Capital of France?', options:['London','Berlin','Paris','Madrid'], correct:2, explanation:'Paris.' },
            { id:8, category:'General Knowledge', difficulty:'Easy', question:'Largest mammal?', options:['Elephant','Blue Whale','Giraffe','Hippo'], correct:1, explanation:'Blue Whale.' },
            { id:9, category:'Mathematics', difficulty:'Medium', question:'12 x 15 = ?', options:['180','175','185','170'], correct:0, explanation:'12 x 15 = 180.' },
            { id:10, category:'Science', difficulty:'Medium', question:'Symbol for gold?', options:['Go','Gd','Au','Ag'], correct:2, explanation:'Au (Aurum).' },
            { id:11, category:'Mathematics', difficulty:'Easy', question:'100 - 37 = ?', options:['63','62','64','61'], correct:0, explanation:'100 - 37 = 63.' },
            { id:12, category:'Science', difficulty:'Easy', question:'The Red Planet?', options:['Venus','Mars','Jupiter','Saturn'], correct:1, explanation:'Mars is the Red Planet.' },
            { id:13, category:'General Knowledge', difficulty:'Easy', question:'Number of continents?', options:['5','6','7','8'], correct:2, explanation:'There are 7 continents.' },
            { id:14, category:'History', difficulty:'Medium', question:'Who built the Taj Mahal?', options:['Akbar','Shah Jahan','Humayun','Aurangzeb'], correct:1, explanation:'Built by Shah Jahan.' },
            { id:15, category:'Mathematics', difficulty:'Medium', question:'25% of 80?', options:['15','20','25','30'], correct:1, explanation:'25% of 80 is 20.' },
            { id:16, category:'English', difficulty:'Easy', question:'Plural of "child"?', options:['childs','childes','children','childs\''], correct:2, explanation:'Children.' },
            { id:17, category:'English', difficulty:'Medium', question:'Synonym for "happy"?', options:['Sad','Joyful','Angry','Tired'], correct:1, explanation:'Joyful means happy.' },
            { id:18, category:'Science', difficulty:'Medium', question:'Liquid to gas process?', options:['Condensation','Evaporation','Precipitation','Sublimation'], correct:1, explanation:'Evaporation.' },
            { id:19, category:'General Knowledge', difficulty:'Medium', question:'Longest river?', options:['Amazon','Nile','Mississippi','Yangtze'], correct:1, explanation:'The Nile River.' },
            { id:20, category:'History', difficulty:'Easy', question:'PCS Academy established year?', options:['2020','2021','2022','2023'], correct:2, explanation:'Established in 2022.' },
            { id:21, category:'Science', difficulty:'Hard', question:'Atomic number of Oxygen?', options:['6','7','8','9'], correct:2, explanation:'Oxygen is atomic number 8.' },
            { id:22, category:'Mathematics', difficulty:'Hard', question:'Derivative of x^2?', options:['x','2x','2x^2','1'], correct:1, explanation:'Power rule: bring down the 2, subtract 1 from exponent.' },
            { id:23, category:'General Knowledge', difficulty:'Medium', question:'Smallest country in the world?', options:['Monaco','Malta','Vatican City','San Marino'], correct:2, explanation:'Vatican City is the smallest.' },
            { id:24, category:'History', difficulty:'Hard', question:'Year of the Battle of Plassey?', options:['1757','1764','1857','1864'], correct:0, explanation:'Fought in 1757.' },
            { id:25, category:'English', difficulty:'Hard', question:'Antonym of "Obsolete"?', options:['Ancient','Current','Outdated','Hidden'], correct:1, explanation:'Current means modern, the opposite of obsolete.' },
            { id:26, category:'Science', difficulty:'Medium', question:'Powerhouse of the cell?', options:['Nucleus','Ribosome','Mitochondria','Golgi'], correct:2, explanation:'Mitochondria generates ATP.' },
            { id:27, category:'Mathematics', difficulty:'Medium', question:'Value of Pi to 2 decimals?', options:['3.12','3.14','3.16','3.18'], correct:1, explanation:'Pi is approximately 3.14.' },
            { id:28, category:'General Knowledge', difficulty:'Hard', question:'Currency of Japan?', options:['Yen','Won','Yuan','Dollar'], correct:0, explanation:'The Japanese Yen.' },
            { id:29, category:'History', difficulty:'Medium', question:'First man on the moon?', options:['Buzz Aldrin','Yuri Gagarin','Neil Armstrong','Michael Collins'], correct:2, explanation:'Neil Armstrong in 1969.' },
            { id:30, category:'Science', difficulty:'Hard', question:'Fastest land animal?', options:['Lion','Cheetah','Leopard','Tiger'], correct:1, explanation:'The Cheetah can reach speeds over 60 mph.' },
            { id:31, category:'Mathematics', difficulty:'Hard', question:'What is 7 cubed (7^3)?', options:['243','343','443','543'], correct:1, explanation:'7 x 7 x 7 = 343.' },
            { id:32, category:'Science', difficulty:'Medium', question:'Which blood cells fight disease?', options:['Red','White','Platelets','Plasma'], correct:1, explanation:'White blood cells form the immune system.' },
            { id:33, category:'History', difficulty:'Hard', question:'Who discovered America in 1492?', options:['Vasco da Gama','Christopher Columbus','Ferdinand Magellan','Marco Polo'], correct:1, explanation:'Christopher Columbus in 1492.' },
            { id:34, category:'General Knowledge', difficulty:'Medium', question:'How many strings on a standard guitar?', options:['4','5','6','7'], correct:2, explanation:'A standard guitar has 6 strings.' },
            { id:35, category:'English', difficulty:'Hard', question:'What is a palindrome?', options:['Word spelt same backwards','A type of poem','A synonym','An exaggeration'], correct:0, explanation:'E.g., racecar or radar.' },
            { id:36, category:'Science', difficulty:'Hard', question:'What is the hardest natural substance?', options:['Gold','Iron','Diamond','Platinum'], correct:2, explanation:'Diamond is the hardest naturally occurring substance.' },
            { id:37, category:'Mathematics', difficulty:'Medium', question:'How many degrees in a circle?', options:['180','270','360','400'], correct:2, explanation:'A full circle has 360 degrees.' },
            { id:38, category:'History', difficulty:'Hard', question:'Who was the iron man of India?', options:['Bhagat Singh','Sardar Patel','Subhas Chandra Bose','Lala Lajpat Rai'], correct:1, explanation:'Sardar Vallabhbhai Patel.' },
            { id:39, category:'General Knowledge', difficulty:'Hard', question:'What is the capital of Australia?', options:['Sydney','Melbourne','Canberra','Perth'], correct:2, explanation:'Canberra is the capital.' },
            { id:40, category:'Science', difficulty:'Medium', question:'Which planet is closest to the sun?', options:['Venus','Earth','Mars','Mercury'], correct:3, explanation:'Mercury is the closest planet.' },
            { id:41, category:'Mathematics', difficulty:'Hard', question:'What is the value of 5 factorial (5!)?', options:['100','120','24','60'], correct:1, explanation:'5! = 5 x 4 x 3 x 2 x 1 = 120.' },
            { id:42, category:'English', difficulty:'Medium', question:'Which is a vowel?', options:['B','C','D','E'], correct:3, explanation:'E is a vowel (A, E, I, O, U).' }
        ];

        this.init();
    }

    init() {
        const self = this;
        
        // Setup Dark Mode toggle
        const themeBtn = document.getElementById('theme-toggle');
        if(themeBtn) themeBtn.addEventListener('click', () => this.toggleTheme());
        
        // Update Lifetime Score UI
        const scoreDisplay = document.getElementById('user-score-display');
        if(scoreDisplay) scoreDisplay.innerText = this.totalLifetimeScore;

        // Splash Screen sequence
        setTimeout(function() {
            self.showScreen('home-screen');
            document.getElementById('main-ui').style.display = 'block';
            
            // Push AdSense dynamically safely
            try { 
                document.querySelectorAll('ins.adsbygoogle').forEach((ins) => {
                    if (!ins.getAttribute('data-adsbygoogle-status')) {
                        (window.adsbygoogle = window.adsbygoogle || []).push({}); 
                    }
                });
            } catch(e) {}
        }, 2500);

        this.setupEventListeners();
    }

    toggleTheme() {
        this.isDarkMode = !this.isDarkMode;
        const themeBtn = document.getElementById('theme-toggle');
        if(this.isDarkMode) {
            document.body.classList.add('dark-theme');
            if(themeBtn) themeBtn.innerText = '☀️';
        } else {
            document.body.classList.remove('dark-theme');
            if(themeBtn) themeBtn.innerText = '🌙';
        }
    }

    showScreen(screenId) {
        document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
        const target = document.getElementById(screenId);
        if (target) target.classList.add('active');
        
        // Active Nav State Update
        document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
        const navBtn = document.getElementById('nav-' + screenId.split('-')[0]);
        if(navBtn) navBtn.classList.add('active');

        this.currentScreen = screenId;
        if (screenId === 'quiz-screen') this.startQuiz();
        window.scrollTo(0, 0);
    }

    setupEventListeners() {
        const self = this;
        document.addEventListener('click', function(e) {
            const btn = e.target.closest('.option-button');
            if (btn && !btn.disabled) self.selectAnswer(btn);
        });
    }

    startQuiz() {
        this.currentQuestion = 0;
        this.score = 0;
        this.userAnswers = [];
        // Randomly select 10 questions from the 42 question bank
        this.quizQuestions = this.questionDB.sort(() => 0.5 - Math.random()).slice(0, this.totalQuestions);

        const wrapper = document.getElementById('quiz-wrapper-dom');
        wrapper.innerHTML = `
            <div class="quiz-header">
                <button onclick="window.quizApp.showScreen('home-screen')" class="super-btn secondary"><span class="btn-icon">←</span> Abort</button>
                <div style="text-align:center;">
                    <h3 style="color:var(--primary); font-weight:800; font-size:1.2rem; margin:0;">Question <span id="q-num">1</span> of ${this.totalQuestions}</h3>
                    <div style="width:150px; height:6px; background:var(--gray-200); border-radius:10px; margin-top:5px; overflow:hidden;">
                        <div id="progress-fill" style="width:10%; height:100%; background:var(--gradient-primary); transition:width 0.3s;"></div>
                    </div>
                </div>
                <h3 style="color:var(--error); font-weight:800; font-size:1.5rem; margin:0;">⏳ <span id="timer">30</span>s</h3>
            </div>
            <div class="question-card">
                <span style="background:var(--sky-blue-100); color:var(--primary-dark); padding:5px 15px; border-radius:20px; font-weight:bold; font-size:0.8rem; text-transform:uppercase;" id="q-cat">Category</span>
                <span id="q-diff" class="badge" style="margin-left:10px;">Easy</span>
                <h2 id="q-text" class="question-title mt-4">Question Text</h2>
            </div>
            <div class="options-grid" id="options-container"></div>
            <div class="quiz-actions">
                <button id="submit-answer" class="super-btn primary large full-width shadow-glow">Submit Answer ✓</button>
                <button id="next-question" class="super-btn primary large full-width shadow-glow" style="display:none;">Next Question ➔</button>
            </div>
        `;

        document.getElementById('submit-answer').addEventListener('click', () => this.submitAnswer());
        document.getElementById('next-question').addEventListener('click', () => this.nextQuestion());

        this.displayQuestion();
    }

    displayQuestion() {
        const q = this.quizQuestions[this.currentQuestion];
        document.getElementById('q-num').innerText = this.currentQuestion + 1;
        document.getElementById('q-cat').innerText = q.category;
        
        const diffBadge = document.getElementById('q-diff');
        diffBadge.innerText = q.difficulty;
        diffBadge.className = `badge ${q.difficulty.toLowerCase()}`;
        
        document.getElementById('q-text').innerText = q.question;
        document.getElementById('progress-fill').style.width = `${((this.currentQuestion + 1) / this.totalQuestions) * 100}%`;

        const container = document.getElementById('options-container');
        container.innerHTML = '';
        
        q.options.forEach((opt, i) => {
            const btn = document.createElement('button');
            btn.className = 'option-button';
            btn.dataset.index = i;
            btn.innerHTML = `<span style="font-weight:900; color:var(--primary); margin-right:15px; background:rgba(14,165,233,0.1); width:35px; height:35px; min-width:35px; display:inline-flex; align-items:center; justify-content:center; border-radius:50%;">${String.fromCharCode(65 + i)}</span> <span>${opt}</span>`;
            container.appendChild(btn);
        });

        this.selectedAnswer = null;
        document.getElementById('submit-answer').style.display = 'inline-flex';
        document.getElementById('next-question').style.display = 'none';
        
        const existingExp = document.getElementById('exp-box');
        if(existingExp) existingExp.remove();

        this.startTimer();
    }

    selectAnswer(btn) {
        document.querySelectorAll('.option-button').forEach(o => o.classList.remove('selected'));
        btn.classList.add('selected');
        this.selectedAnswer = parseInt(btn.dataset.index);
    }

    submitAnswer() {
        if (this.selectedAnswer === null) {
            alert('Please select an answer!');
            return;
        }
        clearInterval(this.timer);
        const q = this.quizQuestions[this.currentQuestion];
        const isCorrect = (this.selectedAnswer === q.correct);

        document.querySelectorAll('.option-button').forEach((btn, i) => {
            btn.disabled = true;
            if (i === q.correct) btn.classList.add('correct');
            else if (i === this.selectedAnswer) btn.classList.add('incorrect');
        });

        if (isCorrect) this.score++;
        
        // Detailed Explanation Injection
        const exp = document.createElement('div');
        exp.id = 'exp-box';
        exp.style.marginTop = '25px';
        exp.style.padding = '20px';
        exp.style.borderRadius = '15px';
        exp.style.background = isCorrect ? 'rgba(34,197,94,0.1)' : 'rgba(239,68,68,0.1)';
        exp.style.borderLeft = isCorrect ? '5px solid var(--success)' : '5px solid var(--error)';
        exp.style.color = 'var(--text-main)';
        exp.innerHTML = `<span style="color:${isCorrect ? 'var(--success)' : 'var(--error)'}; font-size:1.3rem; font-weight:800; display:block; margin-bottom:5px;">${isCorrect ? '✓ Excellent!' : '✗ Not quite.'}</span><span style="color:var(--text-muted); font-size:1rem; line-height:1.5;">${q.explanation}</span>`;
        document.querySelector('.question-card').appendChild(exp);

        document.getElementById('submit-answer').style.display = 'none';
        document.getElementById('next-question').style.display = 'inline-flex';
    }

    nextQuestion() {
        this.currentQuestion++;
        if (this.currentQuestion < this.quizQuestions.length) {
            this.displayQuestion();
        } else {
            this.showResults();
        }
    }

    triggerConfetti() {
        if (typeof confetti === 'function') {
            const duration = 3000;
            const end = Date.now() + duration;
            (function frame() {
                confetti({ particleCount: 5, angle: 60, spread: 55, origin: { x: 0 }, colors: ['#0ea5e9', '#38bdf8'] });
                confetti({ particleCount: 5, angle: 120, spread: 55, origin: { x: 1 }, colors: ['#22c55e', '#ff9800'] });
                if (Date.now() < end) requestAnimationFrame(frame);
            }());
        }
    }

    showResults() {
        clearInterval(this.timer);
        
        // Save to local storage
        this.totalLifetimeScore += this.score;
        localStorage.setItem('pcs_quixler_score', this.totalLifetimeScore);
        const scoreDisplay = document.getElementById('user-score-display');
        if(scoreDisplay) scoreDisplay.innerText = this.totalLifetimeScore;

        const pct = Math.round((this.score / this.quizQuestions.length) * 100);
        const wrapper = document.getElementById('quiz-wrapper-dom');
        
        let msg = "Keep studying and try again!";
        if(pct >= 90) { msg = "Incredible Mastery! Perfect!"; this.triggerConfetti(); }
        else if(pct >= 70) { msg = "Great Job! You have solid knowledge."; if(typeof confetti === 'function') confetti(); }
        else if(pct >= 50) { msg = "Good effort. Room for improvement."; }

        wrapper.innerHTML = `
            <div class="results-container" style="background:var(--bg-card); border-radius:var(--radius-xl); padding:40px 20px; box-shadow:var(--shadow-xl); border: 2px solid var(--primary); text-align:center;">
                <h1 style="font-size:2.5rem; color:var(--primary); font-family:var(--font-secondary); margin-bottom:10px;">Quiz Complete! 🏆</h1>
                <p style="color:var(--text-muted); font-size:1.2rem; font-weight:600; margin-bottom:30px;">${msg}</p>
                
                <div style="width:150px; height:150px; background:var(--gradient-hero); border-radius:50%; display:flex; justify-content:center; align-items:center; margin:0 auto 30px; box-shadow:0 10px 30px rgba(14,165,233,0.4); color:white; font-size:3rem; font-weight:900;">
                    ${pct}%
                </div>
                
                <div style="display:flex; justify-content:space-around; background:var(--sky-blue-50); padding:25px; border-radius:20px; margin-bottom:30px; border: 1px solid var(--sky-blue-100);">
                    <div><span style="font-size:2.5rem; font-weight:900; color:var(--success); display:block; line-height:1;">${this.score}</span><span style="font-size:0.85rem; color:var(--gray-600); font-weight:700; text-transform:uppercase;">Correct</span></div>
                    <div><span style="font-size:2.5rem; font-weight:900; color:var(--error); display:block; line-height:1;">${this.totalQuestions - this.score}</span><span style="font-size:0.85rem; color:var(--gray-600); font-weight:700; text-transform:uppercase;">Incorrect</span></div>
                </div>
                
                <div style="display:flex; flex-direction:column; gap:15px; max-width: 400px; margin: 0 auto;">
                    <button onclick="window.quizApp.startQuiz()" class="super-btn primary large full-width shadow-glow">↺ Play Again</button>
                    <button onclick="window.quizApp.showScreen('home-screen')" class="super-btn secondary large full-width">🏠 Return Home</button>
                    
                    <a href="https://www.effectivegatecpm.com/h4acaqe6?key=4d984694b18d8e6d5e26145d1ac8a80f" target="_blank" class="super-btn warning large full-width glow-pulse" style="margin-top:20px; text-decoration:none; border-color: #ff9800; color: #fff;">
                        <span class="btn-icon">🎁</span> Claim Completion Reward
                    </a>
                </div>
            </div>
        `;
    }

    startTimer() {
        clearInterval(this.timer);
        this.timeLeft = 30;
        document.getElementById('timer').textContent = this.timeLeft;
        document.getElementById('timer').style.color = 'var(--primary)';
        
        this.timer = setInterval(() => {
            this.timeLeft--;
            const t = document.getElementById('timer');
            if(t) {
                t.textContent = this.timeLeft;
                if(this.timeLeft <= 10) t.style.color = 'var(--warning)';
                if(this.timeLeft <= 5) t.style.color = 'var(--error)';
            }
            
            if (this.timeLeft <= 0) {
                clearInterval(this.timer);
                if (this.selectedAnswer === null) {
                    this.nextQuestion();
                } else {
                    this.submitAnswer();
                }
            }
        }, 1000);
    }
}

// Global Boot Execution
document.addEventListener('DOMContentLoaded', function() {
    window.quizApp = new PCSQuizApp();
});
window.showScreen = function(id) { window.quizApp.showScreen(id); };

// ==============================================================================
// SERVICE WORKER REGISTRATION (Required for Adsterra Push & PWA Offline)
// ==============================================================================
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/sw.js')
            .then(function(registration) { 
                console.log('[PCS Quixler] Service Worker Registered Successfully', registration.scope); 
            })
            .catch(function(error) { 
                console.log('[PCS Quixler] Service Worker Registration Failed:', error); 
            });
    });
}
