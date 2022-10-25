# music_spotify_microservice

Part of the app `rest_spotify` for integration with Spotify.

# Переменные окружения

redis_url
SPOTYFI_CLIENT_ID
SPOTYFI_SECRET_KEY
proxy_url

# Запуск сервера

Для старта приложения необходимо прописать в консоли:
```bash
python -m venv venv
pip install -r requirements.txt
uvicorn main:app
```

# Документация

Документация доступна после старта сервера по адресу: localhost:8000/docs
