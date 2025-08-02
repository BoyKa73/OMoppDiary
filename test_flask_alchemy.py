
# Test-Datei, um mit Flask-SQLAlchemy zu üben
# Ziel: Zeige, wie man die Datenbank initialisiert, Tabellen anlegt und Objekte speichert/abfragt

from flask import Flask
# Importiere die Modelle und das db-Objekt aus deinem Hauptprojekt
from models import User, Task, StaticEvent, Quote, Attachment, db

# 1. Flask-App erzeugen
app = Flask(__name__)
# 2. Datenbank-Konfiguration (hier SQLite, Datei heißt test_flask_alchemy.db)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_flask_alchemy.db'
# 3. Geheimschlüssel für Sessions (nicht für die DB, sondern für Flask selbst)
app.config['SECRET_KEY'] = 'geheim'

# 4. Das db-Objekt aus models.py mit der App verknüpfen
#    Im Hintergrund wird jetzt die Engine und die Session für die App konfiguriert
db.init_app(app)

# 5. Mit app.app_context() wird ein Kontext erzeugt, damit Flask weiß, welche App gemeint ist
with app.app_context():
    # 6. Alle Tabellen aus den Modellen werden in der Datenbank angelegt
    db.create_all()
    print("Tabellen wurden erstellt!")

    # 7. Ein neues User-Objekt wird erzeugt und zur Session hinzugefügt
    user = User(username="testuser", password="testpass")
    db.session.add(user)
    # 8. Mit commit() wird das Objekt dauerhaft in die Datenbank geschrieben
    db.session.commit()
    print("User angelegt:", user)

    # 9. Ein Task-Objekt wird erzeugt und dem User zugeordnet (user_id)
    task = Task(content="Test-Task", user_id=user.id)
    db.session.add(task)
    db.session.commit()
    print("Task angelegt:", task)

    # 10. Alle Tasks aus der Datenbank abfragen und ausgeben
    tasks = Task.query.all()
    print("Alle Tasks:", tasks)

# Was passiert im Hintergrund?
# - db.init_app(app): Verknüpft das db-Objekt mit der Flask-App und konfiguriert Engine/Session
# - db.create_all(): Schaut sich alle Modelle an und legt die passenden Tabellen in der DB an
# - db.session: Ist die Schnittstelle, um Objekte zu speichern, abzufragen, zu ändern und zu löschen
# - commit(): Schreibt alle Änderungen aus der Session in die Datenbank