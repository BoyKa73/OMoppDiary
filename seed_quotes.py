# Seeding-Script für die Tabelle Quote
# Führe dieses Skript im Flask-Shell-Kontext oder als separates Python-Skript aus
# ACHTUNG: Die Datenbank, die geseedet wird, hängt davon ab, welche App du importierst!
# Prüfe also, welche App du im Skript importierst!

from models import db, Quote

def seed():
    # Beispiel-Testdaten für die Tabelle Quote
    quotes = [
        Quote(content="Der Weg ist das Ziel.", author="Konfuzius"),
        Quote(content="Carpe diem!", author="Horaz"),
        Quote(content="Das Leben ist zu kurz für später.", author="Unbekannt"),
        Quote(content="Wer kämpft, kann verlieren. Wer nicht kämpft, hat schon verloren.", author="Bertolt Brecht"),
    ]
    db.session.bulk_save_objects(quotes)
    db.session.commit()
    print(f"{len(quotes)} Quotes wurden hinzugefügt.")

if __name__ == "__main__":
    from app import app
    with app.app_context():
        seed()
