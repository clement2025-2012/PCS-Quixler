# Create enhanced JavaScript with improved functionality
js_content = '''// PCS Academy Quiz Application - SUPER Enhanced JavaScript
class PCSQuizApp {
    constructor() {
        this.currentScreen = 'splash-screen';
        this.currentQuestion = 0;
        this.quizQuestions = [];
        this.userAnswers = [];
        this.score = 0;
        this.timer = null;
        this.timeLeft = 30;
        this.selectedAnswer = null;
        this.totalQuestions = 10;
        
        // Enhanced question database with categories and difficulties
        this.questionDB = [
            {
                id: 1,
                category: "Mathematics",
                difficulty: "Easy",
                question: "What is 15 + 27?",
                options: ["42", "41", "43", "40"],
                correct: 0,
                explanation: "15 + 27 = 42. This is basic addition: we add the ones place (5 + 7 = 12, write 2 carry 1) and tens place (1 + 2 + 1 = 4)."
            },
            {
                id: 2,
                category: "Mathematics",
                difficulty: "Easy", 
                question: "What is the square root of 144?",
                options: ["11", "12", "13", "14"],
                correct: 1,
                explanation: "√144 = 12, because 12 × 12 = 144. This is a perfect square that's useful to memorize."
            },
            {
                id: 3,
                category: "Science",
                difficulty: "Easy",
                question: "What gas do plants absorb during photosynthesis?",
                options: ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
                correct: 2,
                explanation: "Plants absorb CO₂ (carbon dioxide) from the air during photosynthesis and use sunlight to convert it into glucose and oxygen."
            },
            {
                id: 4,
                category: "Science",
                difficulty: "Easy",
                question: "How many bones are there in an adult human body?",
                options: ["206", "205", "207", "204"],
                correct: 0,
                explanation: "An adult human skeleton has 206 bones. Babies are born with about 270 bones, but many fuse together as they grow."
            },
            {
                id: 5,
                category: "History",
                difficulty: "Easy",
                question: "Who was the first President of India?",
                options: ["Jawaharlal Nehru", "Dr. Rajendra Prasad", "Mahatma Gandhi", "Sardar Patel"],
                correct: 1,
                explanation: "Dr. Rajendra Prasad was India's first President, serving from 1950 to 1962. He was a key leader in the Indian independence movement."
            },
            {
                id: 6,
                category: "History",
                difficulty: "Easy",
                question: "In which year did India gain independence?",
                options: ["1945", "1946", "1947", "1948"],
                correct: 2,
                explanation: "India gained independence from British rule on August 15, 1947, after years of struggle led by leaders like Gandhi and Nehru."
            },
            {
                id: 7,
                category: "General Knowledge",
                difficulty: "Easy",
                question: "What is the capital of France?",
                options: ["London", "Berlin", "Paris", "Madrid"],
                correct: 2,
                explanation: "Paris is the capital and largest city of France, known for landmarks like the Eiffel Tower and Louvre Museum."
            },
            {
                id: 8,
                category: "General Knowledge",
                difficulty: "Easy",
                question: "What is the largest mammal in the world?",
                options: ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                correct: 1,
                explanation: "The Blue Whale is the largest animal ever known to have lived on Earth, reaching lengths of up to 100 feet."
            },
            {
                id: 9,
                category: "Mathematics",
                difficulty: "Medium",
                question: "What is 12 × 15?",
                options: ["180", "175", "185", "170"],
                correct: 0,
                explanation: "12 × 15 = 180. You can calculate this as (12 × 10) + (12 × 5) = 120 + 60 = 180, or use the standard multiplication method."
            },
            {
                id: 10,
                category: "Science",
                difficulty: "Medium",
                question: "What is the chemical symbol for gold?",
                options: ["Go", "Gd", "Au", "Ag"],
                correct: 2,
                explanation: "The chemical symbol for gold is Au, derived from the Latin word 'aurum' meaning gold."
            },
            {
                id: 11,
                category: "Mathematics",
                difficulty: "Easy",
                question: "What is 100 - 37?",
                options: ["63", "62", "64", "61"],
                correct: 0,
                explanation: "100 - 37 = 63. When subtracting from 100, you can think of it as finding what you need to add to 37 to reach 100."
            },
            {
                id: 12,
                category: "Science",
                difficulty: "Easy",
                question: "Which planet is known as the Red Planet?",
                options: ["Venus", "Mars", "Jupiter", "Saturn"],
                correct: 1,
                explanation: "Mars is known as the Red Planet due to its reddish appearance, caused by iron oxide (rust) on its surface."
            },
            {
                id: 13,
                category: "General Knowledge",
                difficulty: "Easy",
                question: "How many continents are there on Earth?",
                options: ["5", "6", "7", "8"],
                correct: 2,
                explanation: "There are 7 continents: Asia, Africa, North America, South America, Antarctica, Europe, and Australia/Oceania."
            },
            {
                id: 14,
                category: "History",
                difficulty: "Medium",
                question: "Who built the Taj Mahal?",
                options: ["Akbar", "Shah Jahan", "Humayun", "Aurangzeb"],
                correct: 1,
                explanation: "The Taj Mahal was built by Mughal Emperor Shah Jahan in memory of his beloved wife Mumtaz Mahal, completed around 1653."
            },
            {
                id: 15,
                category: "Mathematics",
                difficulty: "Medium",
                question: "What is 25% of 80?",
                options: ["15", "20", "25", "30"],
                correct: 1,
                explanation: "25% of 80 = (25/100) × 80 = 0.25 × 80 = 20. You can also think of 25% as 1/4, so 80 ÷ 4 = 20."
            },
            {
                id: 16,
                category: "English",
                difficulty: "Easy",
                question: "What is the plural form of 'child'?",
                options: ["childs", "childes", "children", "childs'"],
                correct: 2,
                explanation: "The plural form of 'child' is 'children'. This is an irregular plural form in English."
            },
            {
                id: 17,
                category: "English",
                difficulty: "Medium",
                question: "Which word is a synonym for 'happy'?",
                options: ["Sad", "Joyful", "Angry", "Tired"],
                correct: 1,
                explanation: "'Joyful' is a synonym for 'happy' as both words express positive emotions and contentment."
            },
            {
                id: 18,
                category: "Science",
                difficulty: "Medium",
                question: "What is the process by which water changes from liquid to gas?",
                options: ["Condensation", "Evaporation", "Precipitation", "Sublimation"],
                correct: 1,
                explanation: "Evaporation is the process where water changes from liquid to gas due to heat energy."
            },
            {
                id: 19,
                category: "General Knowledge",
                difficulty: "Medium",
                question: "Which is the longest river in the world?",
                options: ["Amazon River", "Nile River", "Mississippi River", "Yangtze River"],
                correct: 1,
                explanation: "The Nile River in Africa is generally considered the longest river in the world at about 6,650 kilometers."
            },
            {
                id: 20,
                category: "History",
                difficulty: "Easy",
                question: "What year was PCS Academy School established?",
                options: ["2020", "2021", "2022", "2023"],
                correct: 2,
                explanation: "PCS Academy School was established in 2022, making it a modern educational institution focused on innovative learning methods."
            }
        ];
        
        this.init();
    }
    
    init() {
        // Show splash screen for 4 seconds with enhanced animation
        this.showSplashScreen();
        setTimeout(() => {
            this.showScreen('home-screen');
        }, 4000);
        
        // Set up event listeners
        this.setupEventListeners();
    }
    
    showSplashScreen() {
        // Enhanced splash screen animations
        const particles = document.querySelectorAll('.particle');
        particles.forEach((particle, index) => {
            particle.style.animationDelay = `${index * 0.5}s`;
        });
    }
    
    setupEventListeners() {
        // Quiz button listeners
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('option-button')) {
                this.selectAnswer(e.target);
            }
        });
        
        const submitButton = document.getElementById('submit-answer');
        const nextButton = document.getElementById('next-question');
        
        if (submitButton) {
            submitButton.addEventListener('click', () => this.submitAnswer());
        }
        
        if (nextButton) {
            nextButton.addEventListener('click', () => this.nextQuestion());
        }
        
        // Enhanced keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (this.currentScreen === 'quiz-screen') {
                switch(e.key.toLowerCase()) {
                    case 'a':
                        this.selectAnswerByIndex(0);
                        break;
                    case 'b':
                        this.selectAnswerByIndex(1);
                        break;
                    case 'c':
                        this.selectAnswerByIndex(2);
                        break;
                    case 'd':
                        this.selectAnswerByIndex(3);
                        break;
                    case 'enter':
                        if (this.selectedAnswer !== null) {
                            this.submitAnswer();
                        }
                        break;
                    case ' ':
                        e.preventDefault();
                        if (this.selectedAnswer !== null) {
                            this.submitAnswer();
                        }
                        break;
                }
            }
        });
        
        // Newsletter form
        const newsletterForm = document.querySelector('.newsletter-form');
        if (newsletterForm) {
            newsletterForm.addEventListener('submit', (e) => {
                e.preventDefault();
                this.handleNewsletterSignup();
            });
        }
    }
    
    showScreen(screenId) {
        // Enhanced screen transitions
        const currentScreenEl = document.querySelector('.screen.active');
        const targetScreenEl = document.getElementById(screenId);
        
        if (currentScreenEl) {
            currentScreenEl.style.opacity = '0';
            currentScreenEl.style.transform = 'translateY(-20px)';
            
            setTimeout(() => {
                currentScreenEl.classList.remove('active');
                
                if (targetScreenEl) {
                    targetScreenEl.classList.add('active');
                    setTimeout(() => {
                        targetScreenEl.style.opacity = '1';
                        targetScreenEl.style.transform = 'translateY(0)';
                    }, 50);
                    
                    this.currentScreen = screenId;
                    
                    // Initialize quiz if entering quiz screen
                    if (screenId === 'quiz-screen') {
                        this.startQuiz();
                    }
                    
                    // Scroll to top
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                }
            }, 300);
        } else {
            // First screen load
            if (targetScreenEl) {
                targetScreenEl.classList.add('active');
                this.currentScreen = screenId;
                
                if (screenId === 'quiz-screen') {
                    this.startQuiz();
                }
            }
        }
    }
    
    startQuiz() {
        // Reset quiz state
        this.currentQuestion = 0;
        this.userAnswers = [];
        this.score = 0;
        this.selectedAnswer = null;
        
        // Shuffle and select questions
        this.quizQuestions = this.shuffleArray([...this.questionDB]).slice(0, this.totalQuestions);
        
        // Show first question
        this.displayQuestion();
        this.updateProgressBar();
        this.startTimer();
    }
    
    displayQuestion() {
        const question = this.quizQuestions[this.currentQuestion];
        
        // Update question counter
        document.getElementById('question-counter').textContent = 
            `Question ${this.currentQuestion + 1} of ${this.quizQuestions.length}`;
        
        // Update category and difficulty
        const categoryEl = document.getElementById('question-category');
        const difficultyEl = document.getElementById('question-difficulty');
        
        if (categoryEl) categoryEl.textContent = question.category;
        if (difficultyEl) {
            difficultyEl.textContent = question.difficulty;
            difficultyEl.className = `question-difficulty ${question.difficulty.toLowerCase()}`;
        }
        
        // Update question text
        document.getElementById('question-text').textContent = question.question;
        
        // Update options with enhanced styling
        const optionsContainer = document.getElementById('options-container');
        optionsContainer.innerHTML = '';
        
        question.options.forEach((option, index) => {
            const button = document.createElement('button');
            button.className = 'option-button';
            button.innerHTML = `
                <div class="option-content">
                    <span class="option-letter">${String.fromCharCode(65 + index)}</span>
                    <span class="option-text">${option}</span>
                </div>
            `;
            button.dataset.index = index;
            optionsContainer.appendChild(button);
        });
        
        // Reset selected answer
        this.selectedAnswer = null;
        
        // Show submit button, hide next button
        document.getElementById('submit-answer').style.display = 'inline-flex';
        document.getElementById('next-question').style.display = 'none';
        
        // Reset and start timer
        this.timeLeft = 30;
        this.startTimer();
        
        // Remove any previous explanations
        const existingExplanation = document.querySelector('.explanation');
        if (existingExplanation) {
            existingExplanation.remove();
        }
    }
    
    selectAnswer(button) {
        // Remove previous selection
        const options = document.querySelectorAll('.option-button');
        options.forEach(opt => opt.classList.remove('selected'));
        
        // Add selection to clicked button with animation
        button.classList.add('selected');
        this.selectedAnswer = parseInt(button.dataset.index);
        
        // Add subtle animation
        button.style.transform = 'scale(1.02)';
        setTimeout(() => {
            button.style.transform = '';
        }, 150);
    }
    
    selectAnswerByIndex(index) {
        const options = document.querySelectorAll('.option-button');
        if (options[index]) {
            this.selectAnswer(options[index]);
        }
    }
    
    submitAnswer() {
        if (this.selectedAnswer === null) {
            this.showNotification('Please select an answer before submitting!', 'warning');
            return;
        }
        
        const question = this.quizQuestions[this.currentQuestion];
        const options = document.querySelectorAll('.option-button');
        
        // Stop timer
        clearInterval(this.timer);
        
        // Show correct/incorrect answers with enhanced animation
        options.forEach((option, index) => {
            option.disabled = true;
            
            if (index === question.correct) {
                option.classList.add('correct');
                this.addCheckmark(option);
            } else if (index === this.selectedAnswer && index !== question.correct) {
                option.classList.add('incorrect');
                this.addXmark(option);
            }
        });
        
        // Record answer
        const isCorrect = this.selectedAnswer === question.correct;
        this.userAnswers.push({
            questionId: question.id,
            question: question.question,
            selected: this.selectedAnswer,
            correct: question.correct,
            isCorrect: isCorrect,
            category: question.category
        });
        
        if (isCorrect) {
            this.score++;
            this.showNotification('Correct! Well done! 🎉', 'success');
        } else {
            this.showNotification('Incorrect. Learn from this! 📚', 'error');
        }
        
        // Show explanation
        this.showExplanation(question.explanation, isCorrect);
        
        // Hide submit button, show next button
        document.getElementById('submit-answer').style.display = 'none';
        document.getElementById('next-question').style.display = 'inline-flex';
    }
    
    addCheckmark(button) {
        const checkmark = document.createElement('div');
        checkmark.className = 'answer-indicator correct';
        checkmark.innerHTML = '✓';
        button.appendChild(checkmark);
    }
    
    addXmark(button) {
        const xmark = document.createElement('div');
        xmark.className = 'answer-indicator incorrect';
        xmark.innerHTML = '✗';
        button.appendChild(xmark);
    }
    
    showExplanation(explanation, isCorrect) {
        // Create enhanced explanation element
        const explanationDiv = document.createElement('div');
        explanationDiv.className = `explanation ${isCorrect ? 'correct' : 'incorrect'}`;
        explanationDiv.innerHTML = `
            <div class="explanation-header">
                <span class="explanation-icon">${isCorrect ? '✓' : '✗'}</span>
                <span class="explanation-status">${isCorrect ? 'Correct!' : 'Incorrect'}</span>
            </div>
            <div class="explanation-text">${explanation}</div>
        `;
        
        // Add to question container
        const questionContainer = document.querySelector('.question-card');
        questionContainer.appendChild(explanationDiv);
        
        // Animate in
        setTimeout(() => {
            explanationDiv.style.opacity = '1';
            explanationDiv.style.transform = 'translateY(0)';
        }, 100);
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
        const progressFill = document.getElementById('progress-fill');
        if (progressFill) {
            const percentage = ((this.currentQuestion + 1) / this.quizQuestions.length) * 100;
            progressFill.style.width = `${percentage}%`;
        }
    }
    
    showResults() {
        const percentage = Math.round((this.score / this.quizQuestions.length) * 100);
        let message = '';
        let emoji = '';
        
        if (percentage >= 90) {
            message = 'Outstanding! Exceptional performance!';
            emoji = '🏆';
        } else if (percentage >= 80) {
            message = 'Excellent work! Great job!';
            emoji = '🎉';
        } else if (percentage >= 70) {
            message = 'Good job! Keep up the good work!';
            emoji = '👍';
        } else if (percentage >= 60) {
            message = 'Fair performance. More practice needed.';
            emoji = '📚';
        } else {
            message = 'Keep studying and try again!';
            emoji = '💪';
        }
        
        // Calculate category performance
        const categoryStats = this.calculateCategoryStats();
        
        const quizContainer = document.querySelector('.quiz-wrapper');
        quizContainer.innerHTML = `
            <div class="results-container">
                <div class="results-header">
                    <h1 class="results-title">Quiz Complete! ${emoji}</h1>
                    <div class="results-score-circle">
                        <div class="score-circle-inner">
                            <span class="score-percentage">${percentage}%</span>
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
                
                <div class="results-message">
                    <h3>${message}</h3>
                </div>
                
                <div class="category-performance">
                    <h3>Performance by Category</h3>
                    <div class="category-stats">
                        ${categoryStats.map(stat => `
                            <div class="category-stat-item">
                                <span class="category-name">${stat.category}</span>
                                <div class="category-bar">
                                    <div class="category-fill" style="width: ${stat.percentage}%"></div>
                                </div>
                                <span class="category-percentage">${stat.percentage}%</span>
                            </div>
                        `).join('')}
                    </div>
                </div>
                
                <div class="results-actions">
                    <button onclick="quizApp.startQuiz()" class="super-btn primary large">
                        <span class="btn-icon">🔄</span>
                        Take Quiz Again
                    </button>
                    <button onclick="quizApp.showScreen('home-screen')" class="super-btn secondary large">
                        <span class="btn-icon">🏠</span>
                        Back to Home
                    </button>
                </div>
            </div>
        `;
        
        // Add results styling
        const style = document.createElement('style');
        style.textContent = `
            .results-container {
                max-width: 600px;
                margin: 0 auto;
                padding: 2rem;
                text-align: center;
                background: white;
                border-radius: 20px;
                box-shadow: 0 20px 40px rgba(41, 182, 246, 0.15);
                border: 1px solid var(--sky-blue-100);
            }
            .results-header { margin-bottom: 2rem; }
            .results-title { 
                font-size: 2rem; 
                color: var(--primary); 
                margin-bottom: 1.5rem;
                font-family: var(--font-secondary);
            }
            .results-score-circle {
                width: 150px;
                height: 150px;
                margin: 0 auto;
                border-radius: 50%;
                background: linear-gradient(135deg, var(--primary), var(--primary-dark));
                display: flex;
                align-items: center;
                justify-content: center;
                box-shadow: 0 10px 30px rgba(41, 182, 246, 0.3);
            }
            .score-circle-inner {
                text-align: center;
                color: white;
            }
            .score-percentage {
                display: block;
                font-size: 2.5rem;
                font-weight: 800;
                font-family: var(--font-secondary);
            }
            .score-label {
                font-size: 1rem;
                opacity: 0.9;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }
            .results-summary {
                display: flex;
                justify-content: space-around;
                margin: 2rem 0;
                padding: 1.5rem;
                background: var(--sky-blue-50);
                border-radius: 15px;
                border: 1px solid var(--sky-blue-100);
            }
            .summary-item {
                text-align: center;
            }
            .summary-number {
                display: block;
                font-size: 1.8rem;
                font-weight: 700;
                color: var(--primary);
                font-family: var(--font-secondary);
            }
            .summary-label {
                font-size: 0.9rem;
                color: var(--gray-600);
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }
            .results-message {
                margin: 2rem 0;
                padding: 1rem;
                background: var(--white);
                border-radius: 10px;
                border-left: 4px solid var(--primary);
            }
            .results-message h3 {
                color: var(--primary);
                font-size: 1.2rem;
            }
            .category-performance {
                margin: 2rem 0;
                text-align: left;
            }
            .category-performance h3 {
                text-align: center;
                color: var(--primary);
                margin-bottom: 1rem;
            }
            .category-stats {
                display: flex;
                flex-direction: column;
                gap: 1rem;
            }
            .category-stat-item {
                display: flex;
                align-items: center;
                gap: 1rem;
            }
            .category-name {
                min-width: 120px;
                font-weight: 600;
                color: var(--gray-700);
            }
            .category-bar {
                flex: 1;
                height: 8px;
                background: var(--gray-200);
                border-radius: 4px;
                overflow: hidden;
            }
            .category-fill {
                height: 100%;
                background: var(--gradient-primary);
                transition: width 1s ease-in-out;
            }
            .category-percentage {
                min-width: 50px;
                font-weight: 600;
                color: var(--primary);
                font-size: 0.9rem;
            }
            .results-actions {
                display: flex;
                gap: 1rem;
                justify-content: center;
                flex-wrap: wrap;
                margin-top: 2rem;
            }
        `;
        document.head.appendChild(style);
    }
    
    calculateCategoryStats() {
        const categories = {};
        
        // Initialize categories
        this.userAnswers.forEach(answer => {
            if (!categories[answer.category]) {
                categories[answer.category] = { correct: 0, total: 0 };
            }
            categories[answer.category].total++;
            if (answer.isCorrect) {
                categories[answer.category].correct++;
            }
        });
        
        // Convert to array with percentages
        return Object.keys(categories).map(category => ({
            category,
            correct: categories[category].correct,
            total: categories[category].total,
            percentage: Math.round((categories[category].correct / categories[category].total) * 100)
        }));
    }
    
    startTimer() {
        clearInterval(this.timer);
        this.timeLeft = 30;
        
        const timerText = document.getElementById('timer');
        const timerProgress = document.getElementById('timer-progress');
        
        this.timer = setInterval(() => {
            this.timeLeft--;
            
            if (timerText) {
                timerText.textContent = this.timeLeft;
            }
            
            // Update circular progress
            if (timerProgress) {
                const percentage = (this.timeLeft / 30) * 100;
                const dashOffset = 100 - percentage;
                timerProgress.style.strokeDashoffset = dashOffset;
            }
            
            // Change color based on time remaining
            if (timerText) {
                if (this.timeLeft <= 5) {
                    timerText.style.color = '#f44336';
                    if (timerProgress) timerProgress.style.stroke = '#f44336';
                } else if (this.timeLeft <= 10) {
                    timerText.style.color = '#ff9800';
                    if (timerProgress) timerProgress.style.stroke = '#ff9800';
                } else {
                    timerText.style.color = '#29b6f6';
                    if (timerProgress) timerProgress.style.stroke = '#29b6f6';
                }
            }
            
            if (this.timeLeft <= 0) {
                clearInterval(this.timer);
                // Auto-submit or move to next question
                if (this.selectedAnswer === null) {
                    this.showNotification('Time\\'s up! Moving to next question.', 'warning');
                    this.nextQuestion();
                } else {
                    this.submitAnswer();
                }
            }
        }, 1000);
    }
    
    showNotification(message, type = 'info') {
        // Create notification element
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <span class="notification-message">${message}</span>
                <button class="notification-close" onclick="this.parentElement.parentElement.remove()">×</button>
            </div>
        `;
        
        // Add to page
        document.body.appendChild(notification);
        
        // Style notification
        const style = document.createElement('style');
        style.textContent = `
            .notification {
                position: fixed;
                top: 20px;
                right: 20px;
                z-index: 10000;
                max-width: 400px;
                padding: 1rem;
                border-radius: 10px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
                animation: slideInRight 0.3s ease-out;
            }
            .notification-success { background: #4caf50; color: white; }
            .notification-error { background: #f44336; color: white; }
            .notification-warning { background: #ff9800; color: white; }
            .notification-info { background: var(--primary); color: white; }
            .notification-content {
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 1rem;
            }
            .notification-close {
                background: none;
                border: none;
                color: inherit;
                font-size: 1.5rem;
                cursor: pointer;
                opacity: 0.7;
            }
            .notification-close:hover { opacity: 1; }
            @keyframes slideInRight {
                from { transform: translateX(100%); opacity: 0; }
                to { transform: translateX(0); opacity: 1; }
            }
        `;
        document.head.appendChild(style);
        
        // Auto-remove after 5 seconds
        setTimeout(() => {
            if (notification.parentElement) {
                notification.style.animation = 'slideOutRight 0.3s ease-in';
                setTimeout(() => notification.remove(), 300);
            }
        }, 5000);
    }
    
    handleNewsletterSignup() {
        const input = document.querySelector('.newsletter-input');
        const email = input.value.trim();
        
        if (email && this.isValidEmail(email)) {
            this.showNotification('Thank you for subscribing! 📧', 'success');
            input.value = '';
        } else {
            this.showNotification('Please enter a valid email address.', 'error');
        }
    }
    
    isValidEmail(email) {
        const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
        return emailRegex.test(email);
    }
    
    shuffleArray(array) {
        const shuffled = [...array];
        for (let i = shuffled.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
        }
        return shuffled;
    }
}

// Global functions for HTML onclick handlers
function showScreen(screenId) {
    if (window.quizApp) {
        window.quizApp.showScreen(screenId);
    }
}

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    window.quizApp = new PCSQuizApp();
    
    // Add smooth scrolling for anchor links
    document.addEventListener('click', function(e) {
        if (e.target.tagName === 'A' && e.target.getAttribute('href')?.startsWith('#')) {
            e.preventDefault();
            const target = document.querySelector(e.target.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
    
    // Add loading animation
    window.addEventListener('load', function() {
        document.body.classList.add('loaded');
    });
    
    // Performance optimization: Lazy load images
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.removeAttribute('data-src');
                        imageObserver.unobserve(img);
                    }
                }
            });
        });

        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }
    
    // Add enhanced interactions
    addEnhancedInteractions();
});

function addEnhancedInteractions() {
    // Add hover effects to cards
    const cards = document.querySelectorAll('.feature-card, .question-card, .contact-method');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // Add click ripple effect to buttons
    const buttons = document.querySelectorAll('.super-btn, .option-button');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('div');
            ripple.className = 'button-ripple';
            
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.cssText = `
                position: absolute;
                width: ${size}px;
                height: ${size}px;
                left: ${x}px;
                top: ${y}px;
                background: rgba(255, 255, 255, 0.3);
                border-radius: 50%;
                transform: scale(0);
                animation: buttonRipple 0.6s linear;
                pointer-events: none;
            `;
            
            this.style.position = 'relative';
            this.style.overflow = 'hidden';
            this.appendChild(ripple);
            
            setTimeout(() => ripple.remove(), 600);
        });
    });
    
    // Add button ripple animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes buttonRipple {
            to {
                transform: scale(2);
                opacity: 0;
            }
        }
        @keyframes slideOutRight {
            from { transform: translateX(0); opacity: 1; }
            to { transform: translateX(100%); opacity: 0; }
        }
    `;
    document.head.appendChild(style);
}

// Add additional utility functions
function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
}

function generateUniqueId() {
    return Date.now().toString(36) + Math.random().toString(36).substr(2);
}

// Export for potential future use
window.PCSQuizApp = PCSQuizApp;'''

with open(f"{project_dir}/app.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("✅ Created enhanced JavaScript with premium functionality and 2022 establishment")