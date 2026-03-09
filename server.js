const express = require('express');
const path = require('path'); 
const app = express();

const PORT = process.env.PORT || 3000;

// 1. Serve your frontend files (tells the server to host your index.html)
app.use(express.static(__dirname));

// 2. YOUR SNIPPET: Serve the ads.txt file perfectly
app.get('/ads.txt', (req, res) => {
  res.sendFile(path.join(__dirname, 'ads.txt'));
});

// 3. Start the server (Always at the bottom)
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
