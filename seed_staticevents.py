# Seeding-Script für die Tabelle StaticEvent
# Führe dieses Skript im Flask-Shell-Kontext oder als separates Python-Skript aus
# ACHTUNG: Die Datenbank, die geseedet wird, hängt davon ab, welche App du importierst!
# Prüfe also, welche App du im Skript importierst!

from models import db, StaticEvent
from datetime import date

def seed():
    # Beispiel-Testdaten für die Tabelle StaticEvent
    events = [
        StaticEvent(title="Sommerferien", start_date=date(2025, 7, 20), end_date=date(2025, 8, 10), color="#fce8b2"),
        StaticEvent(title="Weihnachten", start_date=date(2025, 12, 24), end_date=date(2025, 12, 26), color="#b2e8fc"),
        StaticEvent(title="Neujahr", start_date=date(2026, 1, 1), end_date=date(2026, 1, 1), color="#b2fcb2"),
    ]
    db.session.bulk_save_objects(events)
    db.session.commit()
    print(f"{len(events)} StaticEvents wurden hinzugefügt.")

if __name__ == "__main__":
    from app import app
    with app.app_context():
        seed()
