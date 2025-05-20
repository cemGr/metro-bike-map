FROM python:3.12-slim

WORKDIR /app

# Kopiere Abhängigkeiten und installiere sie
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere alle Projektdateien
COPY . .

# Erstellt die Karte und startet dann Webserver
CMD python main.py && python -m http.server 8000
