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

# --- Hauptseite: Einträge anzeigen und neue Einträge anlegen ---
@app.route("/", methods=["GET", "POST"])
def index():
    # Wenn ein Formular abgeschickt wurde (POST):
    if request.method == "POST":
        # Formulardaten auslesen und bereinigen
        content = request.form.get("content", "").strip()  # Text des Tasks
        people = request.form.get("people", "").strip()    # Beteiligte Personen
        use_today = request.form.get("use_today")            # Checkbox für "heute"
        occurred_on = None

        # Datum und Uhrzeit auslesen
        occurred_on_str = request.form.get("occurred_on", "").strip()
        occurred_time_str = request.form.get("occurred_time", "").strip()

        # 🎯 Pflichtfeld-Validierung: Inhalt darf nicht leer sein
        if not content:
            return "⚠️ Das Inhaltsfeld darf nicht leer sein."

        # Datum und Uhrzeit parsen
        try:
            if use_today:
                # Wenn "heute" gewählt, aktuelles Datum nehmen
                occurred_on = datetime.today()
            else:
                # Datum und Uhrzeit zu einem datetime-Objekt kombinieren
                occurred_on = datetime.strptime(
                    f"{occurred_on_str} {occurred_time_str}", "%Y-%m-%d %H:%M"
                )
        except ValueError:
            # Fehlerhafte Eingabe abfangen
            return "❗ Ungültiges Datum oder Uhrzeit! Format: JJJJ-MM-TT und HH:MM"

        # Task speichern
        try:
            # 📝 Neuen Task anlegen (user_id aktuell hardcodiert)
            new_task = Task(
                content=content,
                people=people,
                occurred_on=occurred_on,
                user_id=1 # TODO: Später dynamisch setzen
            )
            db.session.add(new_task)
            db.session.flush()  # Optional: ID sofort verfügbar machen

            db.session.commit()  # In DB schreiben
            return redirect("/")  # Nach dem Speichern zurück zur Startseite

        except Exception as e:
            db.session.rollback()  # Bei Fehler Änderungen zurücknehmen
            print("Fehler beim Speichern:", e)
            return "❗ Fehler beim Speichern des Eintrags oder der Datei."

    # GET-Request: Alle Tasks für User 1 laden und anzeigen
    tasks = Task.query.filter_by(user_id=1).order_by(Task.occurred_on.desc()).all()
    return render_template("index.html", tasks=tasks, today=datetime.today().date())

# --- NEU: Beispiele für Abfragen und Filtern mit Flask-SQLAlchemy ---
@app.route('/tasks/filter')
def filter_tasks():
    """
    Diese Route zeigt verschiedene Query- und Filter-Beispiele mit Flask-SQLAlchemy.
    Die Ergebnisse werden als JSON ausgegeben.
    """
    # 1. Alle Tasks eines bestimmten Users (z.B. user_id=1)
    tasks_user1 = Task.query.filter_by(user_id=1).all()

    # 2. Tasks nach Kategorie filtern (z.B. "Alltag")
    alltag_tasks = Task.query.filter_by(category="Alltag").all()

    # 3. Tasks nach Stimmung filtern (z.B. "fröhlich")
    happy_tasks = Task.query.filter_by(mood="fröhlich").all()

    # 4. Tasks nach Datum sortieren (absteigend)
    sorted_tasks = Task.query.order_by(Task.occurred_on.desc()).all()

    # 5. Tasks mit Suchbegriff im Inhalt (z.B. alle mit "Park")
    park_tasks = Task.query.filter(Task.content.contains("Park")).all()

    # 6. Kombinierte Filter: Alle "fröhlichen" Tasks von User 1
    happy_user1_tasks = Task.query.filter_by(user_id=1, mood="fröhlich").all()

    # 7. Filter mit mehreren Bedingungen (AND):
    # Alle Tasks von User 1, Kategorie "Alltag", Stimmung "neutral"
    from sqlalchemy import and_
    complex_tasks = Task.query.filter(and_(
        Task.user_id==1,
        Task.category=="Alltag",
        Task.mood=="neutral"
    )).all()

    # 8. Filter mit mehreren Bedingungen (OR):
    from sqlalchemy import or_
    or_tasks = Task.query.filter(or_(
        Task.mood=="fröhlich",
        Task.mood=="traurig"
    )).all()

    # Die Ergebnisse als Dictionary für die JSON-Ausgabe
    result = {
        "tasks_user1": [t.content for t in tasks_user1],
        "alltag_tasks": [t.content for t in alltag_tasks],
        "happy_tasks": [t.content for t in happy_tasks],
        "sorted_tasks": [t.content for t in sorted_tasks],
        "park_tasks": [t.content for t in park_tasks],
        "happy_user1_tasks": [t.content for t in happy_user1_tasks],
        "complex_tasks": [t.content for t in complex_tasks],
        "or_tasks": [t.content for t in or_tasks],
    }
    return jsonify(result)

@app.route('/test/')
def test_route():
    try:
        # Beispiel: Tasks aus DB laden (anpassen, falls nötig)
        tasks = Task.query.all()
        return render_template("test.html", tasks=tasks, today=datetime.today().date())
    except Exception as e:
        print(f"Fehler beim Rendern von /test/: {e}")
        return f"Fehler beim Rendern: {e}", 500

# --- Beispiel für UPDATE mit Flask-SQLAlchemy ---
@app.route('/tasks/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    """
    Aktualisiert einen Task anhand seiner ID.
    Erwartet im POST-Body die Felder 'content' und/oder 'mood'.
    Gibt das aktualisierte Objekt als JSON zurück.
    """
    # Task anhand der ID aus der DB holen
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task nicht gefunden"}), 404

    # Neue Werte aus dem Request holen
    new_content = request.form.get('content')
    new_mood = request.form.get('mood')

    # Felder aktualisieren, falls neue Werte übergeben wurden
    if new_content:
        task.content = new_content
    if new_mood:
        task.mood = new_mood

    # Änderungen speichern
    db.session.commit()

    # Ergebnis zurückgeben
    return jsonify({
        "id": task.id,
        "content": task.content,
        "mood": task.mood
    })

# --- Beispiel für DELETE mit Flask-SQLAlchemy ---
@app.route('/tasks/delete/<int:task_id>', methods=['POST', 'DELETE'])
def delete_task(task_id):
    """
    Löscht einen Task anhand seiner ID.
    Gibt eine Bestätigung als JSON zurück.
    """
    # Task anhand der ID aus der DB holen
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task nicht gefunden"}), 404

    # Task aus der Session entfernen und löschen
    db.session.delete(task)
    db.session.commit()

    # Ergebnis zurückgeben
    return jsonify({
        "message": f"Task {task_id} wurde gelöscht."
    })

# --- Beispiel für CREATE mit Flask-SQLAlchemy ---
@app.route('/tasks/create', methods=['POST'])
def create_task():
    """
    Legt einen neuen Task an.
    Erwartet im POST-Body die Felder 'content', 'people', 'occurred_on', 'occurred_time', 'user_id', 'category', 'mood'.
    Gibt das neue Objekt als JSON zurück.
    """
    # Felder aus dem Request holen
    content = request.form.get('content', '').strip()
    people = request.form.get('people', '').strip()
    occurred_on_str = request.form.get('occurred_on', '').strip()
    occurred_time_str = request.form.get('occurred_time', '').strip()
    user_id = request.form.get('user_id', type=int, default=1)
    category = request.form.get('category', '').strip()
    mood = request.form.get('mood', '').strip()

    # Pflichtfeld-Validierung
    if not content:
        return jsonify({"error": "Das Inhaltsfeld darf nicht leer sein."}), 400

    # Datum und Uhrzeit parsen
    try:
        occurred_on = datetime.strptime(f"{occurred_on_str} {occurred_time_str}", "%Y-%m-%d %H:%M")
    except ValueError:
        occurred_on = None

    # Neuen Task anlegen
    new_task = Task(
        content=content,
        people=people,
        occurred_on=occurred_on,
        user_id=user_id,
        category=category,
        mood=mood
    )
    db.session.add(new_task)
    db.session.commit()

    # Ergebnis zurückgeben
    return jsonify({
        "id": new_task.id,
        "content": new_task.content,
        "people": new_task.people,
        "occurred_on": str(new_task.occurred_on),
        "user_id": new_task.user_id,
        "category": new_task.category,
        "mood": new_task.mood
    })




# --- App-Start ---
if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)


