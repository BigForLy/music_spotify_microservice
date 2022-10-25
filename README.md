# music_spotify_microservice

Part of the app `rest_spotify` for integration with Spotify.

# Переменные окружения

redis_url - Ссылка на Redis сервер

SPOTYFI_CLIENT_ID - Идентификатор приложения пользователя Spotify

SPOTYFI_SECRET_KEY - Секретный ключ приложения пользователя Spotify

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
