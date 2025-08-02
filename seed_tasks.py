
# Seeding-Script für die Tabelle task
# Führe dieses Skript im Flask-Shell-Kontext oder als separates Python-Skript aus
# ACHTUNG: Die Datenbank, die geseedet wird, hängt davon ab, welche App du importierst!
# - Wenn du 'from app import app' verwendest, wird die Datenbank aus app.py (tagebuch.db) verwendet.
# - Wenn du eine andere App importierst (z.B. aus test_flask_alchemy.py), wird die dort konfigurierte DB verwendet.
# Prüfe also, welche App du im Skript importierst!

from models import db, Task
from datetime import datetime, time

# Beispiel-Testdaten für die Tabelle task
seed_tasks = [
    Task(content="Spaziergang im Park", people="Anna", occurred_on=datetime(2025, 8, 1, 15, 0), occurred_at=time(15, 0), user_id=1, category="Alltag", mood="fröhlich"),
    Task(content="Streit mit Kollege", people="Max", occurred_on=datetime(2025, 8, 1, 10, 30), occurred_at=time(10, 30), user_id=1, category="Konflikt", mood="wütend"),
    Task(content="Reflexion über Ziele", people="", occurred_on=datetime(2025, 7, 31, 21, 0), occurred_at=time(21, 0), user_id=1, category="Reflexion", mood="neutral"),
    Task(content="Kaffee mit Lisa", people="Lisa", occurred_on=datetime(2025, 7, 30, 9, 0), occurred_at=time(9, 0), user_id=1, category="Zwischenmenschlich", mood="fröhlich"),
    Task(content="Allein zu Hause gefühlt", people="", occurred_on=datetime(2025, 7, 29, 20, 0), occurred_at=time(20, 0), user_id=1, category="Alltag", mood="traurig"),
    Task(content="Feedbackgespräch Chef", people="Chef", occurred_on=datetime(2025, 7, 28, 14, 0), occurred_at=time(14, 0), user_id=1, category="Konflikt", mood="neutral"),
    Task(content="Tagebuch geschrieben", people="", occurred_on=datetime(2025, 7, 27, 22, 0), occurred_at=time(22, 0), user_id=1, category="Reflexion", mood="fröhlich"),
    Task(content="Einkaufen gewesen", people="", occurred_on=datetime(2025, 7, 26, 17, 0), occurred_at=time(17, 0), user_id=1, category="Alltag", mood="neutral"),
]

def seed():
    # bulk_save_objects fügt alle Objekte aus der Liste auf einmal zur Session hinzu
    # Vorteil: Schneller als viele einzelne .add()-Aufrufe, besonders bei vielen Datensätzen
    db.session.bulk_save_objects(seed_tasks)
    db.session.commit()  # Schreibt alle Tasks in die Datenbank
    print(f"{len(seed_tasks)} Tasks wurden hinzugefügt.")

if __name__ == "__main__":
    # Hier wird die App importiert, die die Datenbank-Konfiguration vorgibt
    # Standard: aus app.py (also tagebuch.db)
    from app import app
    with app.app_context():
        seed()
