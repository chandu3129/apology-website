const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const dbPath = path.join(__dirname, 'apology.db');
const db = new sqlite3.Database(dbPath);

db.serialize(() => {
  // Timeline table
  db.run(`
    CREATE TABLE IF NOT EXISTS timeline (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      date TEXT NOT NULL,
      title TEXT NOT NULL,
      description TEXT NOT NULL,
      emoji TEXT DEFAULT '💕'
    )
  `);

  // Memories table
  db.run(`
    CREATE TABLE IF NOT EXISTS memories (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT NOT NULL,
      description TEXT NOT NULL,
      date_created TEXT DEFAULT CURRENT_TIMESTAMP
    )
  `);

  // Reasons table
  db.run(`
    CREATE TABLE IF NOT EXISTS reasons (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      reason TEXT NOT NULL,
      category TEXT
    )
  `);

  // Messages table
  db.run(`
    CREATE TABLE IF NOT EXISTS messages (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      message TEXT NOT NULL,
      date_created TEXT DEFAULT CURRENT_TIMESTAMP
    )
  `);

  // Insert initial data
  db.run(`
    INSERT OR IGNORE INTO timeline (date, title, description, emoji) VALUES 
    ('2023-01-15', 'Best Friends Start', 'Our beautiful journey began. You became my best friend.', '👯'),
    ('2025-09-29', 'Relationship Begins', 'The day we started dating - September 29, 2025. Best decision ever!', '💕'),
    ('2026-06-26', 'Forever Together', 'Here we are, and I want to make things right. I love you.', '💑')
  `);

  db.run(`
    INSERT OR IGNORE INTO reasons (reason, category) VALUES 
    ('Your beautiful smile makes my day', 'Love'),
    ('The way you laugh at my jokes', 'Happiness'),
    ('Your kindness and compassion', 'Character'),
    ('How you listen to me', 'Support'),
    ('Your strength and courage', 'Inspiration'),
    ('The way you care about others', 'Heart'),
    ('Your intelligence and creativity', 'Mind'),
    ('The memories we share', 'Us'),
    ('Your infectious positivity', 'Energy'),
    ('Forever with you is all I want', 'Future')
  `);

  db.run(`
    INSERT OR IGNORE INTO messages (message) VALUES 
    ('I am deeply sorry for hurting you.'),
    ('You mean the world to me.'),
    ('I promise to do better, to be better.'),
    ('Your love changed my life.'),
    ('I want to spend every moment making you happy.')
  `);
});

module.exports = db;
