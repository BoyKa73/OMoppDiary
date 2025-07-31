
# --- SQLAlchemy Setup ---
from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime

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

# TODO: Weitere Modelle bei Bedarf ergänzen (z.B. User für Authentifizierung)

# --- Weitere Schritte (TODOs) ---
# 1. Entry-Modell wie oben auskommentiert anlegen und Felder anpassen
# 2. Migration durchführen (flask db migrate & upgrade)
# 3. Optional: User-Modell für Login/Authentifizierung ergänzen