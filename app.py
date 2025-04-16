from flask import Flask, send_file
from fetch_events import fetch_and_generate_calendar

app = Flask(__name__)

@app.route("/calendar.ics")
def serve_calendar():
    fetch_and_generate_calendar()
    return send_file("tower_theatre.ics", mimetype="text/calendar")

@app.route("/")
def index():
    return "Tower Theatre Calendar Feed: Subscribe to /calendar.ics"
