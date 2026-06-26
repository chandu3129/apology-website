# Apology Website (Python Flask)

A simple Flask application for a romantic apology website.

## What is included

- `app.py` - Flask backend with SQLite data storage
- `templates/` - Jinja2 templates for the page layout and home view
- `static/style.css` - page styling and responsive design
- `requirements.txt` - Flask dependency

## Run locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the app:
   ```bash
   python app.py
   ```

3. Open the site in your browser:
   ```text
   http://127.0.0.1:5000/
   ```

## Features

- Displays apology message, timeline, love reasons, and messages
- Stores shared memories in SQLite
- Add new memories using the form
- Includes a simple backend API status route at `/api/status`
