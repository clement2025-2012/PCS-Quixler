const express = require('express');
const path    = require('path');

const app  = express();
const PORT = process.env.PORT || 3000;

// Serve ALL files from the root folder (index.html, app.js, style.css, images, etc.)
app.use(express.static(__dirname));

// Serve ads.txt explicitly for Google AdSense
app.get('/ads.txt', (req, res) => {
    res.sendFile(path.join(__dirname, 'ads.txt'));
});

// Catch-all: always return index.html for any unmatched route
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Start server — always at the very bottom
app.listen(PORT, () => {
    console.log(`✅ Server running on http://localhost:${PORT}`);
});
