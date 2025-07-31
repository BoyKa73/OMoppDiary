
# --- SQLAlchemy Setup ---
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Das db-Objekt wird in app.py initialisiert und hier importiert
db = SQLAlchemy()

# --- Datenbankmodelle ---
# Hier werden die Datenbankklassen definiert, die auf Tabellen gemappt werden.

# Beispiel: Tagebucheintrag
# class Entry(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     datum = db.Column(db.Date, nullable=False)
#     titel = db.Column(db.String(100), nullable=False)
#     text = db.Column(db.Text, nullable=False)
#     erstellt_am = db.Column(db.DateTime, default=datetime.utcnow)


# --- Task-Modell ---
# Repräsentiert eine Aufgabe oder ein Ereignis im Tagebuch.
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primärschlüssel
    content = db.Column(db.String(200), nullable=False)  # Beschreibung
    occurred_on = db.Column(db.DateTime)  # Datum des Ereignisses
    occurred_at = db.Column(db.Time)      # Uhrzeit des Ereignisses
    people = db.Column(db.String(100))    # Beteiligte Personen
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Erstellungszeitpunkt
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Fremdschlüssel zu User Tabelle für später
    category = db.Column(db.String(50))   # Kategorie (optional)
    mood = db.Column(db.String(20))       # Stimmung (optional)


# --- StaticEvent-Modell ---
# Repräsentiert ein festes Ereignis (z.B. Ferien, Feiertage).
class StaticEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)  # Titel des Ereignisses
    start_date = db.Column(db.Date, nullable=False)    # Startdatum
    end_date = db.Column(db.Date, nullable=False)      # Enddatum
    color = db.Column(db.String(20), default="#fce8b2")  # Farbe für Kalenderanzeige


# --- Quote-Modell ---
# Repräsentiert ein Zitat, das im Tagebuch angezeigt werden kann.
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)  # Zitattext
    author = db.Column(db.String(100), nullable=True)    # Autor (optional)

# --- Weitere Schritte (TODOs) ---
# 1. User-Modell ergänzen (für Authentifizierung, falls noch nicht vorhanden)
# 2. Entry-Modell für klassische Tagebucheinträge anlegen (siehe Beispiel oben)
# 3. Beziehungen zwischen User und Task/Entry modellieren
# 4. Migrationen durchführen (flask db migrate & upgrade)
# 5. Optional: Validierungen und Methoden für Modelle ergänzen
