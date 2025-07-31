# Module die wir brauchen können
from flask import Flask
# SQLite Anbindung
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, time 
# etwas zum Authentifizieren später, damit niemand anders darauf zugreifen kann und um Authentifizierung zu üben, eine Art Admin Modus


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

app = Flask(__name__)

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tagebuch.db'
app.config['SECRET_KEY'] = 'geheim'

@app.route('/')
def home():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)
