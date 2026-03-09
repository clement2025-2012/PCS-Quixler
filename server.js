// ============================================================
// PCS Academy Quiz App — Node.js / Express Server
// Run: node server.js
// ============================================================
const express = require('express');
const path    = require('path');
const app     = express();
const PORT    = process.env.PORT || 3000;

// Serve all static files from root directory
app.use(express.static(__dirname));

// Explicitly serve ads.txt
app.get('/ads.txt', (req, res) => {
    res.sendFile(path.join(__dirname, 'ads.txt'));
});

// All other routes → index.html (SPA fallback)
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
    console.log(`✅ PCS Academy Quiz running at http://localhost:${PORT}`);
});
