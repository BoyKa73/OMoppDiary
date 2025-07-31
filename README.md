# MoppDiary – Flask Tagebuch App

## Projektbeschreibung
MoppDiary ist eine einfache Tagebuch-Webanwendung auf Basis von Flask und SQLite. Sie ermöglicht das Anlegen, Anzeigen, Bearbeiten und Löschen von Tagebucheinträgen. Die App ist als Lernprojekt für Python, Flask und Datenbankmigrationen gedacht.

## Features
- Einträge mit Datum, Titel und Text speichern
- Einträge anzeigen, bearbeiten und löschen (CRUD)
- Authentifizierung (Admin-Modus, geplant)
- Datenbankmigrationen mit Flask-Migrate (optional)
- Responsive Weboberfläche mit HTML/CSS (geplant)

## Installation
1. Repository klonen:
   ```bash
   git clone <repo-url>
   cd MoppDiary
   ```
2. Virtuelle Umgebung anlegen und aktivieren:
   ```bash
   python -m venv venv
   source venv/bin/activate  # oder venv\Scripts\activate auf Windows
   ```
3. Abhängigkeiten installieren:
   ```bash
   pip install flask flask_sqlalchemy flask_migrate
   ```

## Nutzung
1. App starten:
   ```bash
   python app.py
   ```
2. Im Browser öffnen: [http://localhost:5000](http://localhost:5000)

## Datenbankmigrationen (optional)
Falls Flask-Migrate genutzt wird:
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

## Projektstruktur
```
app.py           # Hauptanwendung
templates/       # HTML-Templates (geplant)
static/          # Statische Dateien (CSS/JS, geplant)
tagebuch.db      # SQLite-Datenbank
```

## Lizenz
MIT License
