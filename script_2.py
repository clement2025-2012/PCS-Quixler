# Create SUPER advanced CSS with stunning sky blue and white design
css_content = '''/* PCS Academy Quiz App - SUPER Sky Blue UI/UX Design */

/* Import Google Fonts for Premium Typography */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@300;400;500;600;700;800&display=swap');

/* Advanced CSS Variables - Sky Blue Theme */
:root {
  /* Sky Blue Color Palette */
  --sky-blue-50: #f0f9ff;
  --sky-blue-100: #e0f2fe;
  --sky-blue-200: #bae6fd;
  --sky-blue-300: #7dd3fc;
  --sky-blue-400: #38bdf8;
  --sky-blue-500: #0ea5e9;
  --sky-blue-600: #0284c7;
  --sky-blue-700: #0369a1;
  --sky-blue-800: #075985;
  --sky-blue-900: #0c4a6e;
  
  /* Primary Theme Colors */
  --primary: #29b6f6;
  --primary-light: #4fc3f7;
  --primary-dark: #0288d1;
  --primary-darker: #01579b;
  
  /* Secondary Colors */
  --secondary: #87ceeb;
  --accent: #1976d2;
  --success: #4caf50;
  --warning: #ff9800;
  --error: #f44336;
  
  /* Neutral Colors */
  --white: #ffffff;
  --gray-50: #fafafa;
  --gray-100: #f5f5f5;
  --gray-200: #eeeeee;
  --gray-300: #e0e0e0;
  --gray-400: #bdbdbd;
  --gray-500: #9e9e9e;
  --gray-600: #757575;
  --gray-700: #616161;
  --gray-800: #424242;
  --gray-900: #212121;
  
  /* Gradient Combinations */
  --gradient-primary: linear-gradient(135deg, var(--sky-blue-400), var(--sky-blue-600));
  --gradient-hero: linear-gradient(135deg, var(--sky-blue-500), var(--primary-dark));
  --gradient-card: linear-gradient(145deg, var(--white), var(--sky-blue-50));
  --gradient-button: linear-gradient(135deg, var(--primary), var(--primary-dark));
  --gradient-background: linear-gradient(180deg, var(--sky-blue-50), var(--white));
  
  /* Advanced Shadows */
  --shadow-xs: 0 1px 2px 0 rgba(41, 182, 246, 0.05);
  --shadow-sm: 0 1px 3px 0 rgba(41, 182, 246, 0.1), 0 1px 2px -1px rgba(41, 182, 246, 0.1);
  --shadow-md: 0 4px 6px -1px rgba(41, 182, 246, 0.1), 0 2px 4px -2px rgba(41, 182, 246, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(41, 182, 246, 0.1), 0 4px 6px -4px rgba(41, 182, 246, 0.1);
  --shadow-xl: 0 20px 25px -5px rgba(41, 182, 246, 0.1), 0 8px 10px -6px rgba(41, 182, 246, 0.1);
  --shadow-2xl: 0 25px 50px -12px rgba(41, 182, 246, 0.25);
  --shadow-inner: inset 0 2px 4px 0 rgba(41, 182, 246, 0.05);
  
  /* Border Radius */
  --radius-sm: 6px;
  --radius-md: 12px;
  --radius-lg: 20px;
  --radius-xl: 24px;
  --radius-2xl: 32px;
  --radius-full: 9999px;
  
  /* Transitions */
  --transition-fast: 0.15s ease-in-out;
  --transition-normal: 0.3s ease-in-out;
  --transition-slow: 0.5s ease-in-out;
  
  /* Typography */
  --font-primary: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-secondary: 'Poppins', sans-serif;
  
  /* Spacing Scale */
  --spacing-xs: 0.5rem;
  --spacing-sm: 0.75rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;
  --spacing-2xl: 3rem;
  --spacing-3xl: 4rem;
}

/* Reset and Base Styles */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  font-size: 16px;
}

body {
  font-family: var(--font-primary);
  line-height: 1.6;
  color: var(--gray-800);
  background: var(--gradient-background);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
}

/* App Container */
#app {
  min-height: 100vh;
  position: relative;
}

/* Screen Management with Smooth Transitions */
.screen {
  display: none;
  min-height: 100vh;
  opacity: 0;
  transform: translateY(20px);
  transition: all var(--transition-normal);
}

.screen.active {
  display: block;
  opacity: 1;
  transform: translateY(0);
}

/* SUPER Enhanced Splash Screen */
#splash-screen {
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--gradient-hero);
  color: var(--white);
  text-align: center;
  position: relative;
  overflow: hidden;
}

.splash-container {
  max-width: 500px;
  padding: var(--spacing-2xl);
  position: relative;
  z-index: 10;
}

.splash-logo-wrapper {
  position: relative;
  margin-bottom: var(--spacing-2xl);
  display: inline-block;
}

.splash-logo {
  width: 140px;
  height: 140px;
  border-radius: var(--radius-full);
  border: 4px solid var(--white);
  box-shadow: var(--shadow-2xl);
  animation: logoFloat 3s ease-in-out infinite;
  position: relative;
  z-index: 2;
}

.logo-glow {
  position: absolute;
  top: -20px;
  left: -20px;
  right: -20px;
  bottom: -20px;
  background: radial-gradient(circle, rgba(255, 255, 255, 0.3), transparent);
  border-radius: var(--radius-full);
  animation: logoGlow 2s ease-in-out infinite alternate;
}

.splash-content {
  margin-bottom: var(--spacing-2xl);
}

.splash-title {
  font-family: var(--font-secondary);
  font-size: 3rem;
  font-weight: 800;
  margin-bottom: var(--spacing-sm);
  text-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
  letter-spacing: -0.02em;
}

.splash-subtitle {
  font-size: 1.5rem;
  font-weight: 500;
  margin-bottom: var(--spacing-md);
  opacity: 0.95;
}

.splash-tagline {
  font-size: 1rem;
  font-weight: 400;
  opacity: 0.8;
  background: rgba(255, 255, 255, 0.2);
  padding: var(--spacing-xs) var(--spacing-md);
  border-radius: var(--radius-full);
  display: inline-block;
}

.loading-container {
  margin-bottom: var(--spacing-xl);
}

.loading-bar {
  width: 100%;
  height: 6px;
  background: rgba(255, 255, 255, 0.3);
  border-radius: var(--radius-full);
  margin-bottom: var(--spacing-md);
  overflow: hidden;
}

.loading-progress {
  height: 100%;
  background: linear-gradient(90deg, var(--white), rgba(255, 255, 255, 0.8));
  border-radius: var(--radius-full);
  animation: loadingProgress 3s ease-in-out;
}

.loading-text {
  font-size: 1rem;
  opacity: 0.9;
  font-weight: 500;
}

/* Floating Particles Animation */
.floating-particles {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.particle {
  position: absolute;
  width: 8px;
  height: 8px;
  background: rgba(255, 255, 255, 0.6);
  border-radius: var(--radius-full);
  animation: particleFloat 8s ease-in-out infinite;
}

.particle:nth-child(1) { top: 20%; left: 10%; animation-delay: 0s; }
.particle:nth-child(2) { top: 60%; left: 20%; animation-delay: 1s; }
.particle:nth-child(3) { top: 30%; left: 80%; animation-delay: 2s; }
.particle:nth-child(4) { top: 80%; left: 70%; animation-delay: 3s; }
.particle:nth-child(5) { top: 10%; left: 60%; animation-delay: 4s; }

/* SUPER Enhanced Header */
.super-header {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  box-shadow: var(--shadow-lg);
  padding: var(--spacing-md) 0;
  position: sticky;
  top: 0;
  z-index: 1000;
  border-bottom: 1px solid var(--sky-blue-100);
}

.header-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 var(--spacing-xl);
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: var(--spacing-lg);
}

.logo-section {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
}

.header-logo {
  width: 60px;
  height: 60px;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
  transition: var(--transition-normal);
}

.header-logo:hover {
  transform: scale(1.05);
  box-shadow: var(--shadow-lg);
}

.logo-text {
  display: flex;
  flex-direction: column;
}

.brand-name {
  font-family: var(--font-secondary);
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--primary);
  line-height: 1.2;
  margin: 0;
}

.brand-tagline {
  font-size: 0.875rem;
  color: var(--gray-600);
  font-weight: 500;
}

.super-nav {
  display: flex;
  gap: var(--spacing-xs);
}

.nav-item {
  display: flex;
  align-items: center;
  gap: var(--spacing-xs);
  text-decoration: none;
  color: var(--gray-700);
  font-weight: 500;
  font-size: 0.95rem;
  padding: var(--spacing-sm) var(--spacing-md);
  border-radius: var(--radius-md);
  transition: var(--transition-fast);
  border: 1px solid transparent;
}

.nav-item:hover {
  background: var(--gradient-primary);
  color: var(--white);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.nav-icon {
  font-size: 1.1em;
}

/* SUPER Hero Section */
.home-main {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 var(--spacing-xl);
}

.super-hero {
  position: relative;
  padding: var(--spacing-3xl) 0;
  margin-bottom: var(--spacing-3xl);
  border-radius: var(--radius-2xl);
  overflow: hidden;
}

.hero-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--gradient-hero);
  z-index: 1;
}

.hero-pattern {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    radial-gradient(circle at 25% 25%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 75% 75%, rgba(255, 255, 255, 0.05) 0%, transparent 50%);
  animation: patternMove 20s linear infinite;
}

.floating-shapes {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
}

.shape {
  position: absolute;
  border-radius: var(--radius-full);
  background: rgba(255, 255, 255, 0.1);
  animation: shapeFloat 15s ease-in-out infinite;
}

.shape-1 {
  width: 100px;
  height: 100px;
  top: 10%;
  left: 10%;
  animation-delay: 0s;
}

.shape-2 {
  width: 150px;
  height: 150px;
  top: 60%;
  right: 10%;
  animation-delay: 5s;
}

.shape-3 {
  width: 80px;
  height: 80px;
  bottom: 20%;
  left: 20%;
  animation-delay: 10s;
}

.hero-content {
  position: relative;
  z-index: 10;
  text-align: center;
  color: var(--white);
  max-width: 900px;
  margin: 0 auto;
  padding: 0 var(--spacing-xl);
}

.hero-badge {
  display: inline-block;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  padding: var(--spacing-sm) var(--spacing-lg);
  border-radius: var(--radius-full);
  font-size: 0.9rem;
  font-weight: 500;
  margin-bottom: var(--spacing-xl);
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.hero-title {
  font-family: var(--font-secondary);
  font-size: clamp(2.5rem, 5vw, 4rem);
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: var(--spacing-lg);
  text-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.highlight {
  background: linear-gradient(135deg, var(--sky-blue-200), var(--white));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subtitle {
  font-weight: 600;
  opacity: 0.95;
  font-size: clamp(1.5rem, 3vw, 2.5rem);
}

.hero-description {
  font-size: 1.2rem;
  line-height: 1.7;
  margin-bottom: var(--spacing-2xl);
  opacity: 0.9;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}

.hero-actions {
  display: flex;
  gap: var(--spacing-lg);
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: var(--spacing-2xl);
}

.hero-stats {
  display: flex;
  justify-content: center;
  gap: var(--spacing-2xl);
  flex-wrap: wrap;
}

.stat-item {
  text-align: center;
}

.stat-number {
  display: block;
  font-family: var(--font-secondary);
  font-size: 2rem;
  font-weight: 700;
  color: var(--white);
  line-height: 1;
}

.stat-label {
  font-size: 0.9rem;
  opacity: 0.8;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* SUPER Enhanced Buttons */
.super-btn {
  display: inline-flex;
  align-items: center;
  gap: var(--spacing-sm);
  padding: var(--spacing-md) var(--spacing-xl);
  font-size: 1rem;
  font-weight: 600;
  text-decoration: none;
  border: none;
  border-radius: var(--radius-lg);
  cursor: pointer;
  transition: var(--transition-fast);
  font-family: var(--font-primary);
  position: relative;
  overflow: hidden;
}

.super-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: var(--transition-normal);
}

.super-btn:hover::before {
  left: 100%;
}

.super-btn.primary {
  background: var(--gradient-button);
  color: var(--white);
  box-shadow: var(--shadow-lg);
}

.super-btn.primary:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-xl);
}

.super-btn.secondary {
  background: var(--white);
  color: var(--primary);
  border: 2px solid var(--primary);
  box-shadow: var(--shadow-md);
}

.super-btn.secondary:hover {
  background: var(--primary);
  color: var(--white);
  transform: translateY(-3px);
  box-shadow: var(--shadow-xl);
}

.super-btn.large {
  padding: var(--spacing-lg) var(--spacing-2xl);
  font-size: 1.1rem;
}

.super-btn.full-width {
  width: 100%;
  justify-content: center;
}

.btn-icon {
  font-size: 1.1em;
}

/* SUPER Enhanced Features Grid */
.super-features {
  padding: var(--spacing-3xl) 0;
  background: var(--white);
  border-radius: var(--radius-2xl);
  box-shadow: var(--shadow-xl);
  margin-bottom: var(--spacing-3xl);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--spacing-xl);
}

.section-header {
  text-align: center;
  margin-bottom: var(--spacing-3xl);
}

.section-title {
  font-family: var(--font-secondary);
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--primary);
  margin-bottom: var(--spacing-md);
  line-height: 1.2;
}

.section-subtitle {
  font-size: 1.2rem;
  color: var(--gray-600);
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.6;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: var(--spacing-xl);
}

.feature-card {
  background: var(--gradient-card);
  border: 1px solid var(--sky-blue-100);
  border-radius: var(--radius-xl);
  padding: var(--spacing-2xl);
  transition: var(--transition-normal);
  position: relative;
  overflow: hidden;
}

.feature-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: var(--gradient-primary);
  transform: scaleX(0);
  transition: var(--transition-normal);
  transform-origin: left;
}

.feature-card:hover::before {
  transform: scaleX(1);
}

.feature-card:hover {
  transform: translateY(-8px);
  box-shadow: var(--shadow-2xl);
  border-color: var(--primary);
}

.card-icon {
  font-size: 3rem;
  margin-bottom: var(--spacing-lg);
  display: block;
}

.card-title {
  font-family: var(--font-secondary);
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--primary);
  margin-bottom: var(--spacing-md);
}

.card-description {
  color: var(--gray-700);
  line-height: 1.6;
  margin-bottom: var(--spacing-lg);
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: var(--spacing-sm);
}

.question-count {
  font-size: 0.9rem;
  color: var(--primary);
  font-weight: 600;
}

.difficulty-badges {
  display: flex;
  gap: var(--spacing-xs);
}

.badge {
  font-size: 0.75rem;
  padding: 2px 8px;
  border-radius: var(--radius-full);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.badge.easy { background: #e8f5e8; color: #2e7d32; }
.badge.medium { background: #fff3e0; color: #f57c00; }
.badge.hard { background: #ffebee; color: #d32f2f; }

.achievement-preview {
  display: flex;
  gap: var(--spacing-xs);
}

.mini-badge {
  font-size: 1.2rem;
}

/* SUPER Enhanced Footer */
.super-footer {
  background: linear-gradient(135deg, var(--gray-900), var(--gray-800));
  color: var(--white);
  padding: var(--spacing-3xl) 0 var(--spacing-xl);
  margin-top: var(--spacing-3xl);
  border-radius: var(--radius-2xl) var(--radius-2xl) 0 0;
}

.footer-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 var(--spacing-xl);
}

.footer-main {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: var(--spacing-2xl);
  margin-bottom: var(--spacing-2xl);
}

.footer-brand {
  display: flex;
  gap: var(--spacing-lg);
  align-items: flex-start;
}

.footer-logo {
  width: 80px;
  height: 80px;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  flex-shrink: 0;
}

.footer-brand-name {
  font-family: var(--font-secondary);
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--sky-blue-300);
  margin-bottom: var(--spacing-xs);
}

.footer-tagline {
  color: var(--gray-300);
  font-size: 0.9rem;
  margin-bottom: var(--spacing-sm);
}

.footer-location {
  color: var(--gray-400);
  font-size: 0.85rem;
}

.footer-section-title {
  font-family: var(--font-secondary);
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--sky-blue-300);
  margin-bottom: var(--spacing-lg);
}

.contact-methods {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-sm);
}

.contact-item {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  color: var(--gray-300);
  text-decoration: none;
  padding: var(--spacing-xs);
  border-radius: var(--radius-sm);
  transition: var(--transition-fast);
}

.contact-item:hover {
  background: rgba(255, 255, 255, 0.1);
  color: var(--white);
  transform: translateX(4px);
}

.contact-icon {
  font-size: 1.1em;
  color: var(--sky-blue-300);
}

.link-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: var(--spacing-sm);
}

.footer-link {
  color: var(--gray-300);
  text-decoration: none;
  padding: var(--spacing-xs) 0;
  transition: var(--transition-fast);
  border-bottom: 1px solid transparent;
}

.footer-link:hover {
  color: var(--sky-blue-300);
  border-bottom-color: var(--sky-blue-300);
}

.newsletter-form {
  display: flex;
  gap: var(--spacing-sm);
  margin-top: var(--spacing-md);
}

.newsletter-input {
  flex: 1;
  padding: var(--spacing-sm) var(--spacing-md);
  border: 1px solid var(--gray-600);
  border-radius: var(--radius-md);
  background: rgba(255, 255, 255, 0.1);
  color: var(--white);
  font-size: 0.9rem;
}

.newsletter-input::placeholder {
  color: var(--gray-400);
}

.newsletter-btn {
  background: var(--gradient-primary);
  color: var(--white);
  border: none;
  padding: var(--spacing-sm) var(--spacing-md);
  border-radius: var(--radius-md);
  font-weight: 500;
  cursor: pointer;
  transition: var(--transition-fast);
}

.newsletter-btn:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.footer-bottom {
  border-top: 1px solid var(--gray-700);
  padding-top: var(--spacing-lg);
}

.footer-bottom-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: var(--spacing-md);
}

.copyright {
  color: var(--gray-400);
  font-size: 0.9rem;
}

.social-links {
  display: flex;
  gap: var(--spacing-sm);
}

.social-link {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: rgba(255, 255, 255, 0.1);
  color: var(--gray-300);
  text-decoration: none;
  border-radius: var(--radius-full);
  transition: var(--transition-fast);
  font-size: 1.2em;
}

.social-link:hover {
  background: var(--primary);
  color: var(--white);
  transform: translateY(-2px);
}

/* SUPER Enhanced Quiz Interface */
.quiz-wrapper {
  max-width: 900px;
  margin: 0 auto;
  padding: var(--spacing-xl);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.quiz-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--spacing-2xl);
  padding: var(--spacing-lg);
  background: var(--white);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-lg);
  border: 1px solid var(--sky-blue-100);
}

.super-back-btn {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  background: var(--gray-100);
  color: var(--gray-700);
  border: none;
  padding: var(--spacing-sm) var(--spacing-lg);
  border-radius: var(--radius-md);
  font-weight: 500;
  cursor: pointer;
  transition: var(--transition-fast);
  text-decoration: none;
}

.super-back-btn:hover {
  background: var(--gray-200);
  transform: translateX(-4px);
}

.quiz-progress-info {
  display: flex;
  align-items: center;
  gap: var(--spacing-xl);
}

.question-indicator {
  text-align: center;
}

.question-number {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--gray-600);
  display: block;
  margin-bottom: var(--spacing-sm);
}

.progress-bar {
  width: 200px;
  height: 6px;
  background: var(--gray-200);
  border-radius: var(--radius-full);
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: var(--gradient-primary);
  border-radius: var(--radius-full);
  transition: width var(--transition-normal);
}

.timer-container {
  position: relative;
}

.timer-circle {
  width: 60px;
  height: 60px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.timer-text {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--primary);
  z-index: 2;
  position: relative;
}

.timer-svg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
}

.quiz-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: var(--spacing-xl);
}

.question-card {
  background: var(--white);
  border: 1px solid var(--sky-blue-100);
  border-radius: var(--radius-xl);
  padding: var(--spacing-2xl);
  box-shadow: var(--shadow-lg);
  position: relative;
}

.question-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: var(--gradient-primary);
  border-radius: var(--radius-xl) var(--radius-xl) 0 0;
}

.question-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--spacing-lg);
}

.question-category {
  background: var(--sky-blue-100);
  color: var(--primary);
  padding: var(--spacing-xs) var(--spacing-md);
  border-radius: var(--radius-full);
  font-size: 0.85rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.question-difficulty {
  padding: var(--spacing-xs) var(--spacing-md);
  border-radius: var(--radius-full);
  font-size: 0.85rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.question-title {
  font-size: 1.4rem;
  line-height: 1.5;
  color: var(--gray-800);
  font-weight: 600;
}

.options-grid {
  display: grid;
  gap: var(--spacing-md);
}

.option-button {
  background: var(--white);
  border: 2px solid var(--gray-200);
  border-radius: var(--radius-lg);
  padding: var(--spacing-lg);
  text-align: left;
  cursor: pointer;
  transition: var(--transition-fast);
  font-size: 1rem;
  font-weight: 500;
  position: relative;
  overflow: hidden;
}

.option-button::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(41, 182, 246, 0.1), transparent);
  transition: var(--transition-normal);
}

.option-button:hover::before {
  left: 100%;
}

.option-button:hover {
  border-color: var(--primary);
  background: var(--sky-blue-50);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.option-button.selected {
  background: var(--gradient-primary);
  color: var(--white);
  border-color: var(--primary);
  box-shadow: var(--shadow-lg);
}

.option-button.correct {
  background: var(--success);
  color: var(--white);
  border-color: var(--success);
}

.option-button.incorrect {
  background: var(--error);
  color: var(--white);
  border-color: var(--error);
}

.quiz-actions {
  text-align: center;
  padding-top: var(--spacing-lg);
}

/* Page Wrapper Styles */
.page-wrapper {
  max-width: 1000px;
  margin: 0 auto;
  padding: var(--spacing-xl);
  min-height: 100vh;
}

.page-header {
  margin-bottom: var(--spacing-2xl);
  padding: var(--spacing-xl);
  background: var(--white);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-lg);
  border: 1px solid var(--sky-blue-100);
}

.page-title-section {
  margin-top: var(--spacing-lg);
}

.page-title {
  font-family: var(--font-secondary);
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--primary);
  margin-bottom: var(--spacing-sm);
  line-height: 1.2;
}

.page-subtitle {
  font-size: 1.2rem;
  color: var(--gray-600);
  line-height: 1.5;
}

.page-content {
  background: var(--white);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-lg);
  border: 1px solid var(--sky-blue-100);
  overflow: hidden;
}

/* About Page Specific Styles */
.about-hero {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: var(--spacing-2xl);
  padding: var(--spacing-2xl);
  background: var(--gradient-card);
  align-items: center;
}

.about-image {
  text-align: center;
}

.about-logo {
  width: 120px;
  height: 120px;
  border-radius: var(--radius-full);
  box-shadow: var(--shadow-lg);
}

.content-title {
  font-family: var(--font-secondary);
  font-size: 1.8rem;
  font-weight: 600;
  color: var(--primary);
  margin-bottom: var(--spacing-md);
}

.content-text {
  font-size: 1.1rem;
  line-height: 1.7;
  color: var(--gray-700);
}

.content-sections {
  padding: var(--spacing-2xl);
}

.content-section {
  margin-bottom: var(--spacing-2xl);
  padding-bottom: var(--spacing-xl);
  border-bottom: 1px solid var(--gray-200);
}

.content-section:last-child {
  border-bottom: none;
  margin-bottom: 0;
}

.section-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--primary);
  margin-bottom: var(--spacing-md);
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
}

.section-text {
  font-size: 1rem;
  line-height: 1.7;
  color: var(--gray-700);
}

.contact-section {
  background: var(--sky-blue-50);
  padding: var(--spacing-xl);
  border-radius: var(--radius-lg);
  border: 1px solid var(--sky-blue-100);
}

.contact-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: var(--spacing-lg);
  margin-top: var(--spacing-lg);
}

.contact-item {
  font-size: 0.95rem;
  line-height: 1.6;
}

.contact-item strong {
  color: var(--primary);
  display: block;
  margin-bottom: var(--spacing-xs);
}

.contact-item a {
  color: var(--primary);
  text-decoration: none;
  font-weight: 500;
}

.contact-item a:hover {
  text-decoration: underline;
}

/* Contact Page Styles */
.contact-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--spacing-3xl);
}

.contact-info-section {
  padding: var(--spacing-2xl);
}

.contact-methods {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-xl);
  margin-top: var(--spacing-xl);
}

.contact-method {
  display: flex;
  gap: var(--spacing-lg);
  padding: var(--spacing-lg);
  background: var(--sky-blue-50);
  border-radius: var(--radius-lg);
  border: 1px solid var(--sky-blue-100);
  transition: var(--transition-fast);
}

.contact-method:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.method-icon {
  font-size: 1.5rem;
  color: var(--primary);
  flex-shrink: 0;
}

.method-details h3 {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--primary);
  margin-bottom: var(--spacing-xs);
}

.contact-link {
  color: var(--primary);
  text-decoration: none;
  font-weight: 500;
}

.contact-link:hover {
  text-decoration: underline;
}

.contact-form-section {
  padding: var(--spacing-2xl);
  background: var(--gray-50);
}

.super-contact-form {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-lg);
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--spacing-lg);
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-sm);
}

.form-label {
  font-weight: 600;
  color: var(--gray-800);
  font-size: 0.95rem;
}

.form-input,
.form-select,
.form-textarea {
  padding: var(--spacing-md);
  border: 2px solid var(--gray-200);
  border-radius: var(--radius-md);
  font-size: 1rem;
  transition: var(--transition-fast);
  font-family: var(--font-primary);
}

.form-input:focus,
.form-select:focus,
.form-textarea:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(41, 182, 246, 0.1);
}

.form-textarea {
  resize: vertical;
  min-height: 120px;
}

/* Policy Pages Styles */
.policy-content {
  padding: var(--spacing-2xl);
}

.policy-meta {
  background: var(--sky-blue-50);
  padding: var(--spacing-lg);
  border-radius: var(--radius-md);
  border-left: 4px solid var(--primary);
  margin-bottom: var(--spacing-2xl);
  font-size: 0.95rem;
  color: var(--gray-700);
}

.policy-sections {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-2xl);
}

.policy-section {
  padding-bottom: var(--spacing-xl);
  border-bottom: 1px solid var(--gray-200);
}

.policy-section:last-child {
  border-bottom: none;
}

.policy-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--primary);
  margin-bottom: var(--spacing-lg);
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
}

.policy-subtitle {
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--gray-800);
  margin: var(--spacing-lg) 0 var(--spacing-md) 0;
}

.policy-text {
  font-size: 1rem;
  line-height: 1.7;
  color: var(--gray-700);
  margin-bottom: var(--spacing-md);
}

.policy-list {
  margin: var(--spacing-md) 0 var(--spacing-lg) var(--spacing-xl);
  color: var(--gray-700);
}

.policy-list li {
  margin-bottom: var(--spacing-sm);
  line-height: 1.6;
}

.contact-info {
  background: var(--sky-blue-50);
  padding: var(--spacing-lg);
  border-radius: var(--radius-md);
  border-left: 4px solid var(--primary);
}

.contact-info p {
  margin-bottom: var(--spacing-sm);
}

.contact-info a {
  color: var(--primary);
  text-decoration: none;
  font-weight: 500;
}

.contact-info a:hover {
  text-decoration: underline;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .header-container {
    padding: 0 var(--spacing-lg);
  }
  
  .home-main {
    padding: 0 var(--spacing-lg);
  }
  
  .hero-content {
    padding: 0 var(--spacing-md);
  }
  
  .features-grid {
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  }
  
  .contact-content {
    grid-template-columns: 1fr;
  }
  
  .about-hero {
    grid-template-columns: 1fr;
    text-align: center;
  }
}

@media (max-width: 768px) {
  :root {
    --spacing-xl: 1.5rem;
    --spacing-2xl: 2rem;
    --spacing-3xl: 2.5rem;
  }
  
  .header-container {
    flex-direction: column;
    text-align: center;
  }
  
  .super-nav {
    flex-wrap: wrap;
    justify-content: center;
  }
  
  .hero-actions {
    flex-direction: column;
    align-items: center;
  }
  
  .hero-stats {
    gap: var(--spacing-lg);
  }
  
  .features-grid {
    grid-template-columns: 1fr;
  }
  
  .footer-main {
    grid-template-columns: 1fr;
    text-align: center;
  }
  
  .quiz-header {
    flex-direction: column;
    gap: var(--spacing-lg);
    text-align: center;
  }
  
  .quiz-progress-info {
    flex-direction: column;
    gap: var(--spacing-md);
  }
  
  .form-row {
    grid-template-columns: 1fr;
  }
  
  .footer-bottom-content {
    flex-direction: column;
    text-align: center;
  }
}

@media (max-width: 480px) {
  .page-wrapper,
  .quiz-wrapper {
    padding: var(--spacing-md);
  }
  
  .hero-content {
    padding: 0;
  }
  
  .feature-card,
  .question-card,
  .page-content {
    padding: var(--spacing-lg);
  }
  
  .splash-container {
    padding: var(--spacing-lg);
  }
  
  .splash-title {
    font-size: 2rem;
  }
  
  .section-title {
    font-size: 2rem;
  }
  
  .page-title {
    font-size: 2rem;
  }
}

/* Animations */
@keyframes logoFloat {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
}

@keyframes logoGlow {
  0% { opacity: 0.5; transform: scale(1); }
  100% { opacity: 0.8; transform: scale(1.05); }
}

@keyframes loadingProgress {
  0% { width: 0%; }
  50% { width: 70%; }
  100% { width: 100%; }
}

@keyframes particleFloat {
  0%, 100% { transform: translateY(0px) rotate(0deg); opacity: 0.6; }
  25% { transform: translateY(-20px) rotate(90deg); opacity: 1; }
  50% { transform: translateY(-10px) rotate(180deg); opacity: 0.8; }
  75% { transform: translateY(-30px) rotate(270deg); opacity: 1; }
}

@keyframes patternMove {
  0% { transform: translateX(0%); }
  100% { transform: translateX(100%); }
}

@keyframes shapeFloat {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  33% { transform: translateY(-20px) rotate(120deg); }
  66% { transform: translateY(10px) rotate(240deg); }
}

/* Utility Classes */
.text-center { text-align: center; }
.text-left { text-align: left; }
.text-right { text-align: right; }

.hidden { display: none !important; }
.visible { display: block !important; }

/* High-contrast mode support */
@media (prefers-contrast: high) {
  :root {
    --primary: #0066cc;
    --primary-dark: #004499;
  }
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

/* Print styles */
@media print {
  .super-header,
  .super-footer,
  .super-btn,
  .quiz-actions {
    display: none !important;
  }
  
  body {
    background: white !important;
  }
  
  .page-content,
  .feature-card,
  .question-card {
    box-shadow: none !important;
    border: 1px solid #ccc !important;
  }
}'''

with open(f"{project_dir}/style.css", "w", encoding="utf-8") as f:
    f.write(css_content)

print("✅ Created SUPER advanced sky blue CSS with premium UI/UX design")