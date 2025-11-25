Student Info Portal — Local Flask demo
This tiny demo serves the static task1.html homepage and receives the login form on /login.

Quick start (Windows / PowerShell):

Create and activate a virtualenv (optional):
python -m venv .venv; .\.venv\Scripts\Activate.ps1
Install dependencies:
pip install -r requirements.txt
Run the Flask app:
python app.py
Open http://127.0.0.1:5000 in your browser. Submit the login form — the server will print the username in the console and show a small confirmation page.
Notes

This is a development demo only and must not be used in production as-is (no authentication, no HTTPS, no CSRF, etc.).
