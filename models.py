
# --- SQLAlchemy Setup ---
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

# Das db-Objekt wird hier initialisiert und in app.py importiert
db = SQLAlchemy()

# --- Datenbankmodelle ---
# Hier werden die Datenbankklassen definiert, die auf Tabellen gemappt werden.


# --- User-Modell ---
# Repräsentiert einen Benutzer (für Authentifizierung und Zuordnung von Tasks).
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Primärschlüssel
    username = db.Column(db.String(100), unique=True, nullable=False)  # Benutzername (eindeutig)
    password = db.Column(db.String(200), nullable=False)  # Passwort (gehasht speichern!)
    is_admin = db.Column(db.Boolean, default=False)  # Admin-Flag
    # Beziehung: Ein User kann mehrere Tasks haben
    tasks = db.relationship("Task", backref="owner", lazy=True)

# --- Task-Modell ---
# Repräsentiert eine Aufgabe oder ein Ereignis im Tagebuch.
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primärschlüssel
    content = db.Column(db.String(200), nullable=False)  # Beschreibung des Tasks
    occurred_on = db.Column(db.DateTime)  # Datum des Ereignisses
    occurred_at = db.Column(db.Time)      # Uhrzeit des Ereignisses
    people = db.Column(db.String(100))    # Beteiligte Personen
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Erstellungszeitpunkt
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Fremdschlüssel zu User
    category = db.Column(db.String(50))   # Kategorie (optional)
    mood = db.Column(db.String(20))       # Stimmung (optional)

    # Beziehung: Ein Task kann mehrere Attachments haben
    attachments = db.relationship('Attachment', back_populates='task', cascade='all, delete-orphan')


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


# --- Attachment-Modell ---
# Repräsentiert eine Datei, die an einen Task angehängt ist.
class Attachment(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primärschlüssel
    filename = db.Column(db.String(255), nullable=False)  # Dateiname
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)  # Fremdschlüssel zu Task

    # Beziehung: Attachment gehört zu genau einem Task
    task = db.relationship('Task', back_populates='attachments')

