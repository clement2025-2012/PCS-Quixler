// ============================================================
// PCS Quixler — Production Node.js / Express Server
// Optimized for Render.com Deployment
// ============================================================
const express = require('express');
const path    = require('path');
const app     = express();
const PORT    = process.env.PORT || 3000;

// Enable CORS for ad networks and static file serving
app.use((req, res, next) => {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

// Serve all static files from root directory
app.use(express.static(__dirname, {
    maxAge: '1d', // Cache static assets for 1 day for better performance
}));

// Explicitly serve ads.txt for AdSense & Adsterra verification
app.get('/ads.txt', (req, res) => {
    res.sendFile(path.join(__dirname, 'ads.txt'));
});

// SPA Fallback: All other routes redirect to index.html
// This prevents 404 errors when users refresh the page on Render
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Start the Server
app.listen(PORT, () => {
    console.log(`===================================================`);
    console.log(`🚀 PCS Quixler Server Live on Port ${PORT}`);
    console.log(`🌍 Ready for Render.com Production Environment`);
    console.log(`===================================================`);
});
