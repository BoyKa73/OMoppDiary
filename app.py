# --- Imports und Setup ---
# Flask: Web-Framework, render_template für das serverseitige rendern von html templates
from flask import Flask, render_template
# SQLAlchemy: ORM für Datenbankzugriff
from flask_sqlalchemy import SQLAlchemy
# Datumsfunktionen
from datetime import datetime, time
# Datenbank-Objekt aus externer models.py
from models import db, Task, StaticEvent, Quote 
# Flask-Migrate: Migrationstool für DB-Schema
from flask_migrate import Migrate
# werden wir garantiert brauchen für die resp der Routen
from flask import jsonify

# --- Flask App & Konfiguration ---
app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tagebuch.db'  # SQLite DB
app.config['SECRET_KEY'] = 'geheim'  # Für Sessions, CSRF etc.

# --- DB & Migration initialisieren ---
db.init_app(app)
migrate = Migrate(app, db)

# alle Tasks holen
tasks = Task.query.all()

# --- Routen ---
@app.route('/')
def home():
    # TODO: Einträge aus DB laden und an Template übergeben
    # Test: 
    # return render_template("index.html", tasks=tasks, today=datetime.today().date())
    return render_template("index.html", today=datetime.today().date())

@app.route('/test')
def home():
    # Einträge aus DB laden und an Template übergeben

    return render_template("test.html", tasks=tasks, today=datetime.today().date())


# --- App-Start ---
if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)


