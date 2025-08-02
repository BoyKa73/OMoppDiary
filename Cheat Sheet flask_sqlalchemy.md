## CREATE 

**Flask-SQLAlchemy Cheat-Sheet: CREATE**

1. Neues Objekt anlegen:
```python
task = Task(
    content="Neuer Task",
    people="Anna",
    occurred_on=datetime(2025, 8, 2, 15, 0),
    user_id=1,
    category="Alltag",
    mood="fröhlich"
)
```

2. Objekt zur Session hinzufügen:
```python
db.session.add(task)
```

3. Änderungen speichern:
```python
db.session.commit()
```

4. Direkt mehrere Objekte anlegen:
```python
tasks = [
    Task(content="Task 1", user_id=1),
    Task(content="Task 2", user_id=1)
]
db.session.bulk_save_objects(tasks)
db.session.commit()
```

5. Pflichtfelder prüfen:
```python
if not content:
    print("Inhalt darf nicht leer sein!")
```

6. Nach dem Commit ist die ID verfügbar:
```python
db.session.add(task)
db.session.commit()
print(task.id)  # Neue ID
```

---

**Merke:**  
- Erst Objekt anlegen, dann mit `add()` zur Session, dann `commit()`.
- Nach dem Commit ist das Objekt dauerhaft in der Datenbank.
- Du kannst die Beispiele direkt in deiner App oder im Flask-Shell-Kontext ausprobieren!

Sag Bescheid, wenn du Praxis, Validierungstipps oder weitere Beispiele möchtest!

## READ bzw. Filter Cheat-Sheet
Hier ist ein kompaktes Cheat-Sheet für die wichtigsten Flask-SQLAlchemy Query-Formen:

---

**Flask-SQLAlchemy Cheat-Sheet (Querying & Filtern)**

1. Alle Einträge einer Tabelle:
```python
Task.query.all()
```

2. Nach Attribut filtern (z.B. user_id):
```python
Task.query.filter_by(user_id=1).all()
```

3. Mehrere Attribute filtern:
```python
Task.query.filter_by(user_id=1, mood="fröhlich").all()
```

4. Mit `filter` und Bedingungen (z.B. AND, OR):
```python
from sqlalchemy import and_, or_
Task.query.filter(and_(Task.user_id==1, Task.mood=="fröhlich")).all()
Task.query.filter(or_(Task.mood=="fröhlich", Task.mood=="traurig")).all()
```

5. Nach Teilstring suchen:
```python
Task.query.filter(Task.content.contains("Park")).all()
```

6. Sortieren:
```python
Task.query.order_by(Task.occurred_on.desc()).all()
Task.query.order_by(Task.occurred_on.asc()).all()
```

7. Einzelnen Eintrag finden:
```python
Task.query.get(1)  # Holt Task mit id=1
```

8. Zählen:
```python
Task.query.filter_by(user_id=1).count()
```

---

**Tipp:** Immer `.all()` für Listen, `.first()` für das erste Ergebnis, `.count()` für Anzahl.

Du kannst dieses Cheat-Sheet als Referenz nutzen und die Beispiele direkt in deiner App ausprobieren! Sag Bescheid, wenn du zu einer Form mehr Details oder Praxis möchtest.

## UPDATE Cheat Sheet
Hier ist dein kompaktes Cheat-Sheet für UPDATE-Operationen mit Flask-SQLAlchemy:

---

**Flask-SQLAlchemy Cheat-Sheet: UPDATE**

1. Ein Objekt aus der DB holen (z.B. mit ID):
```python
task = Task.query.get(1)  # Holt Task mit id=1
```

2. Feld(e) ändern:
```python
task.content = "Neuer Text"
task.mood = "glücklich"
```

3. Änderungen speichern:
```python
db.session.commit()
```

4. Mehrere Felder auf einmal ändern:
```python
task.content = "Text geändert"
task.people = "Anna und Max"
task.mood = "neutral"
db.session.commit()
```

5. Update mit Bedingung (z.B. alle Tasks einer Kategorie):
```python
tasks = Task.query.filter_by(category="Alltag").all()
for t in tasks:
    t.mood = "neutral"
db.session.commit()
```

6. Prüfen, ob Objekt existiert:
```python
task = Task.query.get(99)
if task:
    task.content = "..."
    db.session.commit()
else:
    print("Task nicht gefunden")
```

---

**Merke:**  
- Erst Objekt holen, dann Felder ändern, dann commit!
- Änderungen sind erst nach `db.session.commit()` in der Datenbank.

Du kannst die Beispiele direkt in deiner App oder im Flask-Shell-Kontext ausprobieren! Sag Bescheid, wenn du Praxis oder weitere Tipps möchtest.

## DELETE
Hier ist dein kompaktes Cheat-Sheet für DELETE-Operationen mit Flask-SQLAlchemy:

---

**Flask-SQLAlchemy Cheat-Sheet: DELETE**

1. Ein Objekt aus der DB holen (z.B. mit ID):
```python
task = Task.query.get(1)  # Holt Task mit id=1
```

2. Objekt löschen:
```python
db.session.delete(task)
db.session.commit()
```

3. Vorher prüfen, ob das Objekt existiert:
```python
task = Task.query.get(99)
if task:
    db.session.delete(task)
    db.session.commit()
else:
    print("Task nicht gefunden")
```

4. Mehrere Objekte löschen (z.B. alle Tasks einer Kategorie):
```python
tasks = Task.query.filter_by(category="Alltag").all()
for t in tasks:
    db.session.delete(t)
db.session.commit()
```

5. Komplett alle Tasks löschen:
```python
Task.query.delete()
db.session.commit()
```

---

Hier sind praktische Tipps für das Löschen (Delete) mit Flask-SQLAlchemy:

1. **Immer vorher prüfen, ob das Objekt existiert!**
   Sonst bekommst du einen Fehler, wenn du versuchst, ein nicht vorhandenes Objekt zu löschen.

2. **Löschen ist endgültig:**  
   Nach `db.session.delete(obj)` und `db.session.commit()` ist der Datensatz aus der Datenbank verschwunden. Es gibt kein „Papierkorb“ – also vorsichtig sein!

3. **Fehlerbehandlung einbauen:**  
   Gib dem Nutzer eine Rückmeldung, ob das Löschen erfolgreich war oder das Objekt nicht existierte (wie in deiner Route).

4. **Mehrere Objekte löschen:**  
   Du kannst eine Schleife nutzen, um mehrere Einträge zu löschen, z.B. alle Tasks einer Kategorie.

5. **Verknüpfte Daten beachten:**  
   Wenn du z.B. einen User löschst, prüfe, ob Tasks oder Attachments mit gelöscht werden sollen (Stichwort: „cascade“ in den Beziehungen).

6. **Testen mit Postman oder curl:**  
   Sende eine POST- oder DELETE-Anfrage an deine Route und prüfe die Rückmeldung.

7. **Im Flask-Shell-Kontext üben:**  
   Starte `flask shell` und probiere die Befehle direkt aus:
   ```python
   t = Task.query.get(1)
   db.session.delete(t)
   db.session.commit()
   ```

8. **Nach dem Löschen die Liste neu abfragen:**  
   Zeige dem Nutzer nach dem Löschen die aktualisierte Liste, damit er sieht, dass der Eintrag weg ist.

Wenn du magst, kann ich dir eine kleine Übung oder ein Beispiel für das Löschen mehrerer Tasks geben! Sag einfach Bescheid.