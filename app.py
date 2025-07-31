# --- Imports und Setup ---
# Flask: Web-Framework
from flask import Flask, render_template
# SQLAlchemy: ORM für Datenbankzugriff
from flask_sqlalchemy import SQLAlchemy
# Datumsfunktionen
from datetime import datetime, time
# Datenbank-Objekt aus externer models.py
from models import db 
# Flask-Migrate: Migrationstool für DB-Schema
from flask_migrate import Migrate
# werden wir garantiert brauchen für die resp der Routen
from flask import jsonify

# TODO: Authentifizierung einbauen (z.B. Admin-Modus mit Flask-Login)


# Flask-Migrate Recherche:
# Ja, man kann Prisma und Flask-Migrate in gewisser Weise vergleichen, da beide Tools für das Datenbank-Migrationsmanagement in Webanwendungen genutzt werden, aber sie gehören zu unterschiedlichen Ökosystemen:

# Prisma ist ein ORM (Object-Relational Mapping) und Migrationstool für Node.js/TypeScript-Anwendungen. Es verwaltet Datenbankmodelle, generiert Typen und führt Migrationen durch.
# Flask-Migrate ist ein Migrations-Tool für Flask-Anwendungen (Python), das auf SQLAlchemy und Alembic basiert. Es hilft, Datenbankschemata zu versionieren und Migrationen (z. B. neue Tabellen, Spalten) zu verwalten.
# Beide Tools:

# Erstellen und verwalten Migrationen für Datenbankschemata.
# Erlauben das einfache Anpassen und Updaten der Datenbankstruktur im laufenden Projekt.
# Unterschiede:

# Prisma ist eng mit TypeScript/JavaScript und modernen Node.js-Projekten verbunden.
# Flask-Migrate ist für Python/Flask-Projekte und nutzt SQLAlchemy als ORM.
# Kurz: Beide lösen das gleiche Problem (Migrationen), aber in unterschiedlichen Sprachen und mit unterschiedlicher Integration.


# weitere Schritte, Vorschlag von Copilot:
# Datenbankmodell(e) anlegen:
# Definiere ein SQLAlchemy-Modell für Einträge (z. B. Datum, Titel, Text).

# Routen für CRUD-Operationen:
# Erstelle Routen zum Anzeigen, Hinzufügen, Bearbeiten und Löschen von Tagebucheinträgen.

# Templates nutzen:
# Verwende Jinja2-Templates (Ordner: templates), um HTML-Seiten für die Einträge zu rendern.

# Formulare einbinden:
# Nutze Flask-WTF oder einfache HTML-Formulare für die Eingabe und Bearbeitung.

# Authentifizierung:
# Implementiere einen einfachen Login (z. B. mit Flask-Login), um den Zugriff zu schützen.

# Statische Dateien:
# Lege einen static-Ordner für CSS/JS an, um das Design zu verbessern.


# --- Flask App & Konfiguration ---
app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tagebuch.db'  # SQLite DB
app.config['SECRET_KEY'] = 'geheim'  # Für Sessions, CSRF etc.

# --- DB & Migration initialisieren ---
db.init_app(app)
migrate = Migrate(app, db)


# --- Routen ---
@app.route('/')
def home():
    # TODO: Einträge aus DB laden und an Template übergeben
    return 'Hello, Flask!'


# --- App-Start ---
if __name__ == '__main__':
    app.run(debug=True)

# --- Weitere Schritte (TODOs) ---
# 1. Datenbankmodell für Tagebucheintrag in models.py anlegen (z.B. Datum, Titel, Text)
# 2. CRUD-Routen für Einträge implementieren (anzeigen, hinzufügen, bearbeiten, löschen)
# 3. Templates (Ordner: templates/) für HTML-Ausgabe erstellen
# 4. Formulare für Einträge (Flask-WTF oder HTML)
# 5. Authentifizierung (z.B. Admin-Login mit Flask-Login)
# 6. Statische Dateien (Ordner: static/) für CSS/JS anlegen
