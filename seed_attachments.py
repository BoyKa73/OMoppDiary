# Seeding-Script für die Tabelle Attachment
# Führe dieses Skript im Flask-Shell-Kontext oder als separates Python-Skript aus
# ACHTUNG: Die Datenbank, die geseedet wird, hängt davon ab, welche App du importierst!
# Prüfe also, welche App du im Skript importierst!

from models import db, Attachment

def seed():
    # Beispiel-Testdaten für die Tabelle Attachment
    attachments = [
        Attachment(filename="bild1.jpg", task_id=1),
        Attachment(filename="notiz1.txt", task_id=2),
        Attachment(filename="dokument.pdf", task_id=3),
        Attachment(filename="foto2.png", task_id=4),
    ]
    db.session.bulk_save_objects(attachments)
    db.session.commit()
    print(f"{len(attachments)} Attachments wurden hinzugefügt.")

if __name__ == "__main__":
    from app import app
    with app.app_context():
        seed()
