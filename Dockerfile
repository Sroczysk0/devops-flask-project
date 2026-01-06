# Użycie oficjalnego obrazu Pythona
FROM python:3.11-slim

# Ustawienie katalogu roboczego w kontenerze
WORKDIR /app

# Skopiowanie plików projektu do kontenera
COPY . .

# Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

# Otwarcie portu aplikacji
EXPOSE 5000

# Uruchomienie aplikacji Flask
CMD ["python", "app.py"]
