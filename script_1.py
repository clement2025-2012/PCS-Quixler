# Create SUPER enhanced HTML with sky blue theme and confirmed 2022 establishment
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PCS Academy Quiz App - Educational Learning Platform</title>
    <meta name="description" content="Interactive educational quiz application by PCS Academy School. Test your knowledge in Math, Science, History and more.">
    <meta name="keywords" content="education, quiz, learning, PCS Academy, students, interactive">
    <meta name="author" content="PCS Academy School">
    
    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="favicon.ico">
    <link rel="apple-touch-icon" sizes="180x180" href="assets/PCS-Seal.jpg">
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="PCS Academy Quiz App - Sky Blue Excellence">
    <meta property="og:description" content="Interactive educational quiz application by PCS Academy School with beautiful sky blue design">
    <meta property="og:type" content="website">
    
    <!-- Google Fonts for Enhanced Typography -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- CSS -->
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div id="app">
        <!-- Enhanced Splash Screen -->
        <div id="splash-screen" class="screen active">
            <div class="splash-container">
                <div class="splash-logo-wrapper">
                    <img src="assets/PCS-Seal.jpg" alt="PCS Academy School" class="splash-logo">
                    <div class="logo-glow"></div>
                </div>
                <div class="splash-content">
                    <h1 class="splash-title">PCS ACADEMY</h1>
                    <p class="splash-subtitle">Educational Quiz App</p>
                    <div class="splash-tagline">Excellence in Education Since 2022</div>
                </div>
                <div class="loading-container">
                    <div class="loading-bar">
                        <div class="loading-progress"></div>
                    </div>
                    <p class="loading-text">Loading Amazing Experience...</p>
                </div>
                <div class="floating-particles">
                    <div class="particle"></div>
                    <div class="particle"></div>
                    <div class="particle"></div>
                    <div class="particle"></div>
                    <div class="particle"></div>
                </div>
            </div>
        </div>

        <!-- Enhanced Home Screen -->
        <div id="home-screen" class="screen">
            <header class="super-header">
                <div class="header-container">
                    <div class="header-left">
                        <div class="logo-section">
                            <img src="assets/PCS-Seal.jpg" alt="PCS Academy" class="header-logo">
                            <div class="logo-text">
                                <h1 class="brand-name">PCS ACADEMY</h1>
                                <span class="brand-tagline">Educational Excellence</span>
                            </div>
                        </div>
                    </div>
                    <nav class="super-nav">
                        <a href="#" onclick="showScreen('quiz-screen')" class="nav-item">
                            <span class="nav-icon">🎯</span>
                            Start Quiz
                        </a>
                        <a href="#" onclick="showScreen('about-screen')" class="nav-item">
                            <span class="nav-icon">ℹ️</span>
                            About
                        </a>
                        <a href="#" onclick="showScreen('contact-screen')" class="nav-item">
                            <span class="nav-icon">📞</span>
                            Contact
                        </a>
                        <a href="#" onclick="showScreen('privacy-screen')" class="nav-item">
                            <span class="nav-icon">🔒</span>
                            Privacy
                        </a>
                    </nav>
                </div>
            </header>

            <main class="home-main">
                <!-- Hero Section with Super Design -->
                <section class="super-hero">
                    <div class="hero-background">
                        <div class="hero-pattern"></div>
                        <div class="floating-shapes">
                            <div class="shape shape-1"></div>
                            <div class="shape shape-2"></div>
                            <div class="shape shape-3"></div>
                        </div>
                    </div>
                    <div class="hero-content">
                        <div class="hero-badge">🏆 Since 2022 - Educational Excellence</div>
                        <h1 class="hero-title">
                            Welcome to <span class="highlight">PCS Academy</span><br>
                            <span class="hero-subtitle">Interactive Learning Platform</span>
                        </h1>
                        <p class="hero-description">
                            Discover the joy of learning with our comprehensive quiz platform. 
                            Test your knowledge across multiple subjects with beautifully designed 
                            interactive quizzes that make education engaging and fun.
                        </p>
                        <div class="hero-actions">
                            <button class="super-btn primary" onclick="showScreen('quiz-screen')">
                                <span class="btn-icon">🚀</span>
                                Start Learning Journey
                            </button>
                            <button class="super-btn secondary" onclick="showScreen('about-screen')">
                                <span class="btn-icon">📚</span>
                                Learn More
                            </button>
                        </div>
                        <div class="hero-stats">
                            <div class="stat-item">
                                <span class="stat-number">200+</span>
                                <span class="stat-label">Questions</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-number">5</span>
                                <span class="stat-label">Subjects</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-number">2022</span>
                                <span class="stat-label">Established</span>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Enhanced Features Grid -->
                <section class="super-features">
                    <div class="container">
                        <div class="section-header">
                            <h2 class="section-title">Explore Learning Categories</h2>
                            <p class="section-subtitle">Choose from our comprehensive range of subjects designed for interactive learning</p>
                        </div>
                        <div class="features-grid">
                            <div class="feature-card math">
                                <div class="card-icon">🧮</div>
                                <h3 class="card-title">Mathematics</h3>
                                <p class="card-description">Enhance your mathematical skills with problems ranging from basic arithmetic to advanced concepts and problem-solving techniques.</p>
                                <div class="card-footer">
                                    <span class="question-count">50+ Questions</span>
                                    <div class="difficulty-badges">
                                        <span class="badge easy">Easy</span>
                                        <span class="badge medium">Medium</span>
                                        <span class="badge hard">Hard</span>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="feature-card science">
                                <div class="card-icon">🔬</div>
                                <h3 class="card-title">Science</h3>
                                <p class="card-description">Explore the wonders of Physics, Chemistry, Biology, and Earth Science through engaging interactive questions and experiments.</p>
                                <div class="card-footer">
                                    <span class="question-count">60+ Questions</span>
                                    <div class="difficulty-badges">
                                        <span class="badge easy">Easy</span>
                                        <span class="badge medium">Medium</span>
                                        <span class="badge hard">Hard</span>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="feature-card history">
                                <div class="card-icon">🏛️</div>
                                <h3 class="card-title">History</h3>
                                <p class="card-description">Journey through time with questions covering World History, Indian Heritage, and Ancient Civilizations that shaped our world.</p>
                                <div class="card-footer">
                                    <span class="question-count">40+ Questions</span>
                                    <div class="difficulty-badges">
                                        <span class="badge easy">Easy</span>
                                        <span class="badge medium">Medium</span>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="feature-card english">
                                <div class="card-icon">📖</div>
                                <h3 class="card-title">English</h3>
                                <p class="card-description">Master the English language with comprehensive grammar, vocabulary, and reading comprehension exercises.</p>
                                <div class="card-footer">
                                    <span class="question-count">35+ Questions</span>
                                    <div class="difficulty-badges">
                                        <span class="badge easy">Easy</span>
                                        <span class="badge medium">Medium</span>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="feature-card gk">
                                <div class="card-icon">🌍</div>
                                <h3 class="card-title">General Knowledge</h3>
                                <p class="card-description">Broaden your understanding with questions covering current affairs, geography, sports, and fascinating facts about our world.</p>
                                <div class="card-footer">
                                    <span class="question-count">55+ Questions</span>
                                    <div class="difficulty-badges">
                                        <span class="badge easy">Easy</span>
                                        <span class="badge medium">Medium</span>
                                        <span class="badge hard">Hard</span>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="feature-card achievements">
                                <div class="card-icon">🏆</div>
                                <h3 class="card-title">Achievements</h3>
                                <p class="card-description">Earn badges, track your progress, unlock achievements, and compete with friends in our gamified learning environment.</p>
                                <div class="card-footer">
                                    <span class="question-count">Progress Tracking</span>
                                    <div class="achievement-preview">
                                        <span class="mini-badge">🥇</span>
                                        <span class="mini-badge">📊</span>
                                        <span class="mini-badge">⭐</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </main>

            <!-- Super Enhanced Footer -->
            <footer class="super-footer">
                <div class="footer-container">
                    <div class="footer-main">
                        <div class="footer-brand">
                            <img src="assets/PCS-Seal.jpg" alt="PCS Academy" class="footer-logo">
                            <div class="brand-info">
                                <h3 class="footer-brand-name">PCS Academy School</h3>
                                <p class="footer-tagline">Excellence in Education Since 2022</p>
                                <p class="footer-location">📍 Ambah, Madhya Pradesh, India</p>
                            </div>
                        </div>
                        
                        <div class="footer-contact">
                            <h4 class="footer-section-title">Get in Touch</h4>
                            <div class="contact-methods">
                                <a href="tel:+919977365777" class="contact-item">
                                    <span class="contact-icon">📞</span>
                                    +91 9977365777
                                </a>
                                <a href="tel:+918269950030" class="contact-item">
                                    <span class="contact-icon">📞</span>
                                    +91 8269950030
                                </a>
                                <a href="mailto:pcsacademyschool@gmail.com" class="contact-item">
                                    <span class="contact-icon">✉️</span>
                                    pcsacademyschool@gmail.com
                                </a>
                            </div>
                        </div>
                        
                        <div class="footer-links">
                            <h4 class="footer-section-title">Important Links</h4>
                            <div class="link-grid">
                                <a href="#" onclick="showScreen('privacy-screen')" class="footer-link">Privacy Policy</a>
                                <a href="#" onclick="showScreen('terms-screen')" class="footer-link">Terms of Service</a>
                                <a href="#" onclick="showScreen('about-screen')" class="footer-link">About Us</a>
                                <a href="#" onclick="showScreen('contact-screen')" class="footer-link">Contact</a>
                                <a href="#" onclick="showScreen('quiz-screen')" class="footer-link">Start Quiz</a>
                                <a href="#" class="footer-link">Help & Support</a>
                            </div>
                        </div>
                        
                        <div class="footer-newsletter">
                            <h4 class="footer-section-title">Stay Connected</h4>
                            <p class="newsletter-description">Get updates about new quizzes and educational content</p>
                            <div class="newsletter-form">
                                <input type="email" placeholder="Enter your email" class="newsletter-input">
                                <button class="newsletter-btn">Subscribe</button>
                            </div>
                        </div>
                    </div>
                    
                    <div class="footer-bottom">
                        <div class="footer-bottom-content">
                            <p class="copyright">© 2025 PCS Academy School. All rights reserved. | Established 2022</p>
                            <div class="social-links">
                                <a href="#" class="social-link">📧</a>
                                <a href="#" class="social-link">📱</a>
                                <a href="#" class="social-link">🌐</a>
                            </div>
                        </div>
                    </div>
                </div>
            </footer>
        </div>

        <!-- Enhanced Quiz Screen -->
        <div id="quiz-screen" class="screen">
            <div class="quiz-wrapper">
                <div class="quiz-header">
                    <button onclick="showScreen('home-screen')" class="super-back-btn">
                        <span class="btn-icon">←</span>
                        Back to Home
                    </button>
                    <div class="quiz-progress-info">
                        <div class="question-indicator">
                            <span id="question-counter" class="question-number">Question 1 of 10</span>
                            <div class="progress-bar">
                                <div class="progress-fill" id="progress-fill"></div>
                            </div>
                        </div>
                        <div class="timer-container">
                            <div class="timer-circle">
                                <div class="timer-text" id="timer">30</div>
                                <svg class="timer-svg" viewBox="0 0 36 36">
                                    <circle cx="18" cy="18" r="16" fill="none" stroke="#e0f2fe" stroke-width="2"/>
                                    <circle id="timer-progress" cx="18" cy="18" r="16" fill="none" stroke="#29b6f6" stroke-width="2" stroke-dasharray="100 100" stroke-dashoffset="0"/>
                                </svg>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="quiz-content">
                    <div class="question-card">
                        <div class="question-header">
                            <span class="question-category" id="question-category">Mathematics</span>
                            <span class="question-difficulty" id="question-difficulty">Easy</span>
                        </div>
                        <h2 id="question-text" class="question-title">Loading question...</h2>
                    </div>
                    
                    <div class="options-grid" id="options-container">
                        <!-- Options will be populated by JavaScript -->
                    </div>
                    
                    <div class="quiz-actions">
                        <button id="submit-answer" class="super-btn primary large">
                            <span class="btn-icon">✓</span>
                            Submit Answer
                        </button>
                        <button id="next-question" class="super-btn primary large" style="display: none;">
                            <span class="btn-icon">→</span>
                            Next Question
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Enhanced About Screen -->
        <div id="about-screen" class="screen">
            <div class="page-wrapper">
                <div class="page-header">
                    <button onclick="showScreen('home-screen')" class="super-back-btn">
                        <span class="btn-icon">←</span>
                        Back to Home
                    </button>
                    <div class="page-title-section">
                        <h1 class="page-title">About PCS Academy School</h1>
                        <p class="page-subtitle">Excellence in Education Since 2022</p>
                    </div>
                </div>
                
                <div class="page-content">
                    <div class="about-hero">
                        <div class="about-image">
                            <img src="assets/PCS-Seal.jpg" alt="PCS Academy School" class="about-logo">
                        </div>
                        <div class="about-intro">
                            <h2 class="content-title">Our Educational Vision</h2>
                            <p class="content-text">
                                PCS Academy School, proudly established in <strong>2022</strong>, represents a new era in educational excellence. 
                                We are committed to providing quality education through innovative teaching methods and 
                                technology-enhanced learning experiences that prepare students for future success.
                            </p>
                        </div>
                    </div>
                    
                    <div class="content-sections">
                        <div class="content-section">
                            <h2 class="section-title">🎯 Our Mission</h2>
                            <p class="section-text">
                                Since our establishment in 2022, PCS Academy has been dedicated to nurturing young minds 
                                and preparing them for the challenges of tomorrow. We believe in creating an environment 
                                where learning is engaging, interactive, and accessible to all students.
                            </p>
                        </div>
                        
                        <div class="content-section">
                            <h2 class="section-title">🚀 Educational Excellence</h2>
                            <p class="section-text">
                                In just three years since our founding in 2022, we have rapidly grown to become a leading 
                                educational institution in Ambah, Madhya Pradesh. Our comprehensive approach combines 
                                traditional teaching methods with cutting-edge technology to create truly engaging learning experiences.
                            </p>
                        </div>
                        
                        <div class="content-section">
                            <h2 class="section-title">💻 Technology-Enhanced Learning</h2>
                            <p class="section-text">
                                This interactive quiz application exemplifies our commitment to digital education. 
                                We provide state-of-the-art learning tools that make education accessible, engaging, 
                                and effective for students across all age groups and learning styles.
                            </p>
                        </div>
                        
                        <div class="contact-section">
                            <h2 class="section-title">📞 Contact Information</h2>
                            <div class="contact-grid">
                                <div class="contact-item">
                                    <strong>School Name:</strong> PCS Academy School
                                </div>
                                <div class="contact-item">
                                    <strong>Established:</strong> 2022
                                </div>
                                <div class="contact-item">
                                    <strong>Location:</strong> Ambah, Madhya Pradesh, India
                                </div>
                                <div class="contact-item">
                                    <strong>Phone Numbers:</strong><br>
                                    <a href="tel:+919977365777">+91 9977365777</a><br>
                                    <a href="tel:+918269950030">+91 8269950030</a>
                                </div>
                                <div class="contact-item">
                                    <strong>Email:</strong><br>
                                    <a href="mailto:pcsacademyschool@gmail.com">pcsacademyschool@gmail.com</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Contact Screen -->
        <div id="contact-screen" class="screen">
            <div class="page-wrapper">
                <div class="page-header">
                    <button onclick="showScreen('home-screen')" class="super-back-btn">
                        <span class="btn-icon">←</span>
                        Back to Home
                    </button>
                    <div class="page-title-section">
                        <h1 class="page-title">Contact PCS Academy</h1>
                        <p class="page-subtitle">Get in touch with us - We'd love to hear from you!</p>
                    </div>
                </div>
                
                <div class="page-content">
                    <div class="contact-content">
                        <div class="contact-info-section">
                            <h2 class="section-title">📞 Get in Touch</h2>
                            
                            <div class="contact-methods">
                                <div class="contact-method">
                                    <div class="method-icon">📞</div>
                                    <div class="method-details">
                                        <h3>Phone Numbers</h3>
                                        <p><a href="tel:+919977365777" class="contact-link">+91 9977365777</a></p>
                                        <p><a href="tel:+918269950030" class="contact-link">+91 8269950030</a></p>
                                    </div>
                                </div>
                                
                                <div class="contact-method">
                                    <div class="method-icon">✉️</div>
                                    <div class="method-details">
                                        <h3>Email Address</h3>
                                        <p><a href="mailto:pcsacademyschool@gmail.com" class="contact-link">pcsacademyschool@gmail.com</a></p>
                                    </div>
                                </div>
                                
                                <div class="contact-method">
                                    <div class="method-icon">📍</div>
                                    <div class="method-details">
                                        <h3>Address</h3>
                                        <p>PCS Academy School<br>Ambah, Madhya Pradesh, India</p>
                                    </div>
                                </div>
                                
                                <div class="contact-method">
                                    <div class="method-icon">🕒</div>
                                    <div class="method-details">
                                        <h3>Office Hours</h3>
                                        <p>Monday - Saturday: 9:00 AM - 3:00 PM<br>Sunday: Closed</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="contact-form-section">
                            <h2 class="section-title">💬 Send us a Message</h2>
                            <form class="super-contact-form" action="mailto:pcsacademyschool@gmail.com" method="post" enctype="text/plain">
                                <div class="form-row">
                                    <div class="form-group">
                                        <label for="name" class="form-label">Full Name</label>
                                        <input type="text" id="name" name="name" class="form-input" required>
                                    </div>
                                    <div class="form-group">
                                        <label for="email" class="form-label">Email Address</label>
                                        <input type="email" id="email" name="email" class="form-input" required>
                                    </div>
                                </div>
                                
                                <div class="form-group">
                                    <label for="subject" class="form-label">Subject</label>
                                    <select id="subject" name="subject" class="form-select" required>
                                        <option value="">Select a subject</option>
                                        <option value="Admission Inquiry">🎓 Admission Inquiry</option>
                                        <option value="Academic Support">📚 Academic Support</option>
                                        <option value="Technical Issues">🔧 Technical Issues</option>
                                        <option value="General Questions">❓ General Questions</option>
                                    </select>
                                </div>
                                
                                <div class="form-group">
                                    <label for="message" class="form-label">Message</label>
                                    <textarea id="message" name="message" rows="5" class="form-textarea" required placeholder="Tell us how we can help you..."></textarea>
                                </div>
                                
                                <button type="submit" class="super-btn primary large full-width">
                                    <span class="btn-icon">📤</span>
                                    Send Message
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Privacy Policy Screen -->
        <div id="privacy-screen" class="screen">
            <div class="page-wrapper">
                <div class="page-header">
                    <button onclick="showScreen('home-screen')" class="super-back-btn">
                        <span class="btn-icon">←</span>
                        Back to Home
                    </button>
                    <div class="page-title-section">
                        <h1 class="page-title">Privacy Policy</h1>
                        <p class="page-subtitle">How we protect and handle your information</p>
                    </div>
                </div>
                
                <div class="page-content">
                    <div class="policy-content">
                        <div class="policy-meta">
                            <strong>Last Updated:</strong> October 11, 2025<br>
                            <strong>Effective Date:</strong> Since our establishment in 2022
                        </div>
                        
                        <div class="policy-sections">
                            <section class="policy-section">
                                <h2 class="policy-title">🛡️ Introduction</h2>
                                <p class="policy-text">
                                    PCS Academy School ("we," "our," or "us"), established in 2022, is committed to protecting your privacy. 
                                    This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you 
                                    visit our educational quiz application and interact with our services.
                                </p>
                            </section>
                            
                            <section class="policy-section">
                                <h2 class="policy-title">📊 Information We Collect</h2>
                                <h3 class="policy-subtitle">Personal Information</h3>
                                <ul class="policy-list">
                                    <li>Name and contact information when you register or contact us</li>
                                    <li>Educational progress and quiz performance data</li>
                                    <li>Device information and browser details for optimization</li>
                                    <li>IP address and general location data for security</li>
                                </ul>
                                
                                <h3 class="policy-subtitle">Cookies and Tracking Technologies</h3>
                                <p class="policy-text">
                                    We use cookies and similar technologies to enhance your experience and analyze website usage:
                                </p>
                                <ul class="policy-list">
                                    <li>Essential cookies for website functionality</li>
                                    <li>Analytics cookies to understand user behavior and improve our services</li>
                                    <li>Third-party advertising cookies (Google AdSense) for relevant advertisements</li>
                                </ul>
                            </section>
                            
                            <section class="policy-section">
                                <h2 class="policy-title">🤝 Third-Party Services</h2>
                                <h3 class="policy-subtitle">Google AdSense</h3>
                                <p class="policy-text">
                                    We use Google AdSense to display relevant advertisements. Google may use cookies and other 
                                    technologies to serve ads based on your prior visits to our website or other websites. 
                                    You can opt out of personalized advertising by visiting Google's Ad Settings.
                                </p>
                                
                                <h3 class="policy-subtitle">Analytics Services</h3>
                                <p class="policy-text">
                                    We may use Google Analytics or similar services to analyze website traffic and user behavior, 
                                    helping us improve our educational services and user experience.
                                </p>
                            </section>
                            
                            <section class="policy-section">
                                <h2 class="policy-title">🎯 How We Use Your Information</h2>
                                <ul class="policy-list">
                                    <li>Provide and maintain our educational services and quiz platform</li>
                                    <li>Track academic progress and personalize learning experiences</li>
                                    <li>Communicate with students, parents, and educators</li>
                                    <li>Improve our website functionality and educational content</li>
                                    <li>Ensure security and prevent fraud or misuse</li>
                                    <li>Comply with legal obligations and educational standards</li>
                                </ul>
                            </section>
                            
                            <section class="policy-section">
                                <h2 class="policy-title">⚖️ Your Rights</h2>
                                <p class="policy-text">Under applicable privacy laws (GDPR, CCPA, and Indian privacy regulations), you have the right to:</p>
                                <ul class="policy-list">
                                    <li>Access and review your personal data</li>
                                    <li>Correct inaccurate or incomplete information</li>
                                    <li>Request deletion of your personal data</li>
                                    <li>Object to certain types of data processing</li>
                                    <li>Data portability and the right to receive your data</li>
                                    <li>Withdraw consent for data processing where applicable</li>
                                </ul>
                            </section>
                            
                            <section class="policy-section">
                                <h2 class="policy-title">👶 Children's Privacy</h2>
                                <p class="policy-text">
                                    We comply with COPPA (Children's Online Privacy Protection Act) regulations. We do not knowingly 
                                    collect personal information from children under 13 without verifiable parental consent. If we 
                                    learn that we have collected information from a child under 13 without proper consent, we will 
                                    delete that information promptly.
                                </p>
                            </section>
                            
                            <section class="policy-section">
                                <h2 class="policy-title">📞 Contact Us</h2>
                                <p class="policy-text">
                                    If you have any questions about this Privacy Policy or our data practices, please contact us:
                                </p>
                                <div class="contact-info">
                                    <p><strong>Email:</strong> <a href="mailto:pcsacademyschool@gmail.com">pcsacademyschool@gmail.com</a></p>
                                    <p><strong>Phone:</strong> <a href="tel:+919977365777">+91 9977365777</a>, <a href="tel:+918269950030">+91 8269950030</a></p>
                                    <p><strong>Address:</strong> PCS Academy School, Ambah, Madhya Pradesh, India</p>
                                    <p><strong>Established:</strong> 2022</p>
                                </div>
                            </section>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Terms of Service Screen -->
        <div id="terms-screen" class="screen">
            <div class="page-wrapper">
                <div class="page-header">
                    <button onclick="showScreen('home-screen')" class="super-back-btn">
                        <span class="btn-icon">←</span>
                        Back to Home
                    </button>
                    <div class="page-title-section">
                        <h1 class="page-title">Terms of Service</h1>
                        <p class="page-subtitle">Terms and conditions for using our platform</p>
                    </div>
                </div>
                
                <div class="page-content">
                    <div class="policy-content">
                        <div class="policy-meta">
                            <strong>Last Updated:</strong> October 11, 2025<br>
                            <strong>Effective Since:</strong> Our establishment in 2022
                        </div>
                        
                        <div class="policy-sections">
                            <section class="policy-section">
                                <h2 class="policy-title">📋 Acceptance of Terms</h2>
                                <p class="policy-text">
                                    By accessing and using the PCS Academy Quiz Application and related services, you accept and agree to be bound by the terms and provisions of this agreement. PCS Academy School, established in 2022, provides these educational services subject to the following terms.
                                </p>
                            </section>
                            
                            <section class="policy-section">
                                <h2 class="policy-title">🎓 Educational Use</h2>
                                <p class="policy-text">
                                    This platform is designed exclusively for educational purposes. Users agree to use the quiz application solely for learning, academic improvement, and educational advancement. The content is designed to support formal education and personal development.
                                </p>
                            </section>
                            
                            <section class="policy-section">
                                <h2 class="policy-title">👤 User Responsibilities</h2>
                                <ul class="policy-list">
                                    <li>Provide accurate and truthful information when registering or interacting with our platform</li>
                                    <li>Use the platform responsibly, ethically, and in accordance with educational best practices</li>
                                    <li>Respect intellectual property rights of all educational content and materials</li>
                                    <li>Not attempt to hack, manipulate, or interfere with the normal operation of our systems</li>
                                    <li>Not share inappropriate, offensive, or harmful content through our platform</li>
                                    <li>Maintain the confidentiality of any account credentials and report unauthorized access</li>
                                </ul>
                            </section>
                            
                            <section class="policy-section">
                                <h2 class="policy-title">📚 Intellectual Property</h2>
                                <p class="policy-text">
                                    All content, including but not limited to questions, explanations, educational materials, design elements, and software, is the exclusive property of PCS Academy School (established 2022) and is protected by copyright, trademark, and other intellectual property laws. Unauthorized reproduction or distribution is strictly prohibited.
                                </p>
                            </section>
                            
                            <section class="policy-section">
                                <h2 class="policy-title">⚠️ Limitation of Liability</h2>
                                <p class="policy-text">
                                    PCS Academy School shall not be liable for any indirect, incidental, special, consequential, or punitive damages resulting from your use of the platform, including but not limited to loss of data, educational outcomes, or technical difficulties. Our educational services are provided "as is" for educational enhancement purposes.
                                </p>
                            </section>
                            
                            <section class="policy-section">
                                <h2 class="policy-title">🔄 Modifications</h2>
                                <p class="policy-text">
                                    We reserve the right to modify these terms at any time to reflect changes in our services, legal requirements, or educational policies. Continued use of the platform after any modifications constitutes acceptance of the updated terms.
                                </p>
                            </section>
                            
                            <section class="policy-section">
                                <h2 class="policy-title">⚖️ Governing Law</h2>
                                <p class="policy-text">
                                    These terms and conditions are governed by the laws of Madhya Pradesh, India, and any disputes shall be subject to the jurisdiction of courts in Madhya Pradesh.
                                </p>
                            </section>
                            
                            <section class="policy-section">
                                <h2 class="policy-title">📞 Contact Information</h2>
                                <p class="policy-text">
                                    For questions regarding these terms or any legal matters related to our educational services, please contact us:
                                </p>
                                <div class="contact-info">
                                    <p><strong>Email:</strong> <a href="mailto:pcsacademyschool@gmail.com">pcsacademyschool@gmail.com</a></p>
                                    <p><strong>Phone:</strong> <a href="tel:+919977365777">+91 9977365777</a>, <a href="tel:+918269950030">+91 8269950030</a></p>
                                    <p><strong>Address:</strong> PCS Academy School, Ambah, Madhya Pradesh, India</p>
                                    <p><strong>Established:</strong> 2022</p>
                                </div>
                            </section>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- JavaScript -->
    <script src="app.js"></script>
</body>
</html>'''

with open(f"{project_dir}/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ Created SUPER enhanced HTML with sky blue theme and 2022 establishment confirmed")