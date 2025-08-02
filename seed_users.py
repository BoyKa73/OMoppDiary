# Seeding-Script für die Tabelle User
# Führe dieses Skript im Flask-Shell-Kontext oder als separates Python-Skript aus
# ACHTUNG: Die Datenbank, die geseedet wird, hängt davon ab, welche App du importierst!
# Prüfe also, welche App du im Skript importierst!

from models import db, User

def seed():
    # Beispiel-Testdaten für die Tabelle User
    users = [
        User(username="Anna", password="hashed_pw1", is_admin=False),
        User(username="Max", password="hashed_pw2", is_admin=False),
        User(username="Lisa", password="hashed_pw3", is_admin=False),
        User(username="Chef", password="hashed_pw4", is_admin=True),
    ]
    db.session.bulk_save_objects(users)
    db.session.commit()
    print(f"{len(users)} User wurden hinzugefügt.")

if __name__ == "__main__":
    from app import app
    with app.app_context():
        seed()
