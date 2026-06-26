import sqlite3
from pathlib import Path
from flask import Flask, g, redirect, render_template, request, url_for

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / 'app.db'

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['DATABASE'] = str(DB_PATH)

SCHEMA = '''
CREATE TABLE IF NOT EXISTS timeline (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_date TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    icon TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS reasons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    reason TEXT NOT NULL,
    category TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS memories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
'''

DEFAULT_TIMELINE = [
    ('2023-01-15', 'Best Friends Start', 'The day our friendship began and everything changed for the better.', '👯'),
    ('2025-09-29', 'Relationship Begins', 'We took the next step together on September 29, 2025. That day still feels like magic.', '💕'),
    ('2026-06-26', 'Today and Tomorrow', 'I am here to make things right, to listen, and to build our future together.', '💑')
]

DEFAULT_REASONS = [
    ('Your smile brightens my hardest days.', 'Love'),
    ('You always support me, even when I make mistakes.', 'Support'),
    ('Your kindness inspires me to become a better person.', 'Character'),
    ('Your laughter is my favorite sound.', 'Joy'),
    ('You are my safe place and my greatest adventure.', 'Heart')
]

DEFAULT_MESSAGES = [
    ('I am deeply sorry for everything I did wrong.'),
    ('You are the most important person in my life.'),
    ('I will keep learning and growing with you.'),
    ('Your forgiveness means the world to me.'),
    ('I want to make every day better than the last.'),
]

DEFAULT_MEMORIES = [
    ('First Walk Together', 'We walked under the warm city lights and talked for hours. I still remember how safe I felt.'),
    ('First Date', 'That first date when I realized I wanted to be with you forever.'),
]


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
        db.row_factory = sqlite3.Row
    return db


def init_db():
    db = get_db()
    db.executescript(SCHEMA)

    if not db.execute('SELECT COUNT(*) FROM timeline').fetchone()[0]:
        db.executemany('INSERT INTO timeline(event_date, title, description, icon) VALUES (?, ?, ?, ?)', DEFAULT_TIMELINE)

    if not db.execute('SELECT COUNT(*) FROM reasons').fetchone()[0]:
        db.executemany('INSERT INTO reasons(reason, category) VALUES (?, ?)', DEFAULT_REASONS)

    if not db.execute('SELECT COUNT(*) FROM messages').fetchone()[0]:
        db.executemany('INSERT INTO messages(message) VALUES (?)', [(m,) for m in DEFAULT_MESSAGES])

    if not db.execute('SELECT COUNT(*) FROM memories').fetchone()[0]:
        db.executemany('INSERT INTO memories(title, description) VALUES (?, ?)', DEFAULT_MEMORIES)

    db.commit()


@app.teardown_appcontext
def close_db(exception=None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.before_first_request
def prepare_database():
    init_db()


@app.route('/')
def home():
    db = get_db()
    timeline = db.execute('SELECT * FROM timeline ORDER BY event_date ASC').fetchall()
    reasons = db.execute('SELECT * FROM reasons ORDER BY id').fetchall()
    messages = db.execute('SELECT * FROM messages ORDER BY created_at ASC').fetchall()
    memories = db.execute('SELECT * FROM memories ORDER BY created_at DESC').fetchall()
    return render_template('index.html', timeline=timeline, reasons=reasons, messages=messages, memories=memories)


@app.route('/add-memory', methods=['POST'])
def add_memory():
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    if title and description:
        db = get_db()
        db.execute('INSERT INTO memories(title, description) VALUES (?, ?)', (title, description))
        db.commit()
    return redirect(url_for('home'))


@app.route('/api/status')
def api_status():
    return {'status': 'ok', 'message': 'The apology app is running.'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
