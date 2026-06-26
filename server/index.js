const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const path = require('path');
const db = require('./database');

const app = express();
const PORT = 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, '../public')));

// Routes
app.get('/api/timeline', (req, res) => {
  db.all('SELECT * FROM timeline ORDER BY date ASC', (err, rows) => {
    if (err) {
      res.status(500).json({ error: err.message });
      return;
    }
    res.json(rows);
  });
});

app.get('/api/memories', (req, res) => {
  db.all('SELECT * FROM memories ORDER BY date_created DESC', (err, rows) => {
    if (err) {
      res.status(500).json({ error: err.message });
      return;
    }
    res.json(rows);
  });
});

app.post('/api/memories', (req, res) => {
  const { title, description } = req.body;
  db.run(
    'INSERT INTO memories (title, description) VALUES (?, ?)',
    [title, description],
    function(err) {
      if (err) {
        res.status(500).json({ error: err.message });
        return;
      }
      res.json({ id: this.lastID, title, description });
    }
  );
});

app.get('/api/reasons', (req, res) => {
  db.all('SELECT * FROM reasons', (err, rows) => {
    if (err) {
      res.status(500).json({ error: err.message });
      return;
    }
    res.json(rows);
  });
});

app.get('/api/messages', (req, res) => {
  db.all('SELECT * FROM messages ORDER BY date_created ASC', (err, rows) => {
    if (err) {
      res.status(500).json({ error: err.message });
      return;
    }
    res.json(rows);
  });
});

app.post('/api/messages', (req, res) => {
  const { message } = req.body;
  db.run(
    'INSERT INTO messages (message) VALUES (?)',
    [message],
    function(err) {
      if (err) {
        res.status(500).json({ error: err.message });
        return;
      }
      res.json({ id: this.lastID, message });
    }
  );
});

app.listen(PORT, () => {
  console.log(`❤️ Apology Website running on http://localhost:${PORT}`);
  console.log('Making things right... 💕');
});
