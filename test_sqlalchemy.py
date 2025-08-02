# Test-Datei, um mit SQLAlchemy zu üben, kann später gelöscht werden oder in die gitignore
from sqlalchemy import create_engine
engine = create_engine('sqlite:///test.db')
connection = engine.connect()
print("Verbindung erfolgreich:", connection)
connection.close()