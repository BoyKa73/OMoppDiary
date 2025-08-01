# --- Imports und Setup ---
# Flask: Web-Framework, render_template für das serverseitige rendern von html templates
from flask import Flask, render_template, request, redirect
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


# --- Routen ---
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form.get("content", "").strip()
        people = request.form.get("people", "").strip()
        use_today = request.form.get("use_today")
        occurred_on = None

        occurred_on_str = request.form.get("occurred_on", "").strip()
        occurred_time_str = request.form.get("occurred_time", "").strip()

        # 🎯 Basisvalidierung: Pflichtfeld content
        if not content:
            return "⚠️ Das Inhaltsfeld darf nicht leer sein."

        try:
            if use_today:
                occurred_on = datetime.today()
            else:
                # ⏳ Kombiniere Datum + Uhrzeit zu datetime-Objekt
                occurred_on = datetime.strptime(
                    f"{occurred_on_str} {occurred_time_str}",
                    "%Y-%m-%d %H:%M"
                )
        except ValueError:
            return "❗ Ungültiges Datum oder Uhrzeit! Format: JJJJ-MM-TT und HH:MM"

        try:
            # 📝 Task erzeugen
            new_task = Task(
                content=content,
                people=people,
                occurred_on=occurred_on,
                user_id=1 #erstmal hardcoded
            )
            db.session.add(new_task)
            db.session.flush()

            db.session.commit()
            return redirect("/")

        except Exception as e:
            db.session.rollback()
            print("Fehler beim Speichern:", e)
            return "❗ Fehler beim Speichern des Eintrags oder der Datei."

    tasks = Task.query.filter_by(user_id=1).order_by(Task.occurred_on.desc()).all()
    return render_template("index.html", tasks=tasks, today=datetime.today().date())


@app.route('/test/')
def test_route():
    try:
        # Beispiel: Tasks aus DB laden (anpassen, falls nötig)
        tasks = Task.query.all()
        return render_template("test.html", tasks=tasks, today=datetime.today().date())
    except Exception as e:
        print(f"Fehler beim Rendern von /test/: {e}")
        return f"Fehler beim Rendern: {e}", 500




# --- App-Start ---
if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)


