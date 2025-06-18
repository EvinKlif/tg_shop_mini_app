FROM python:3.12-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем pyproject.toml и poetry.lock
COPY pyproject.toml .
COPY poetry.lock .

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false

# Копируем папку App внутрь контейнера
COPY App ./App

RUN mkdir -p /app/App/media
# Устанавливаем зависимости через Poetry
RUN poetry install --no-interaction --no-ansi

# Открываем порт
EXPOSE 8000

# Запускаем приложение
CMD ["sh", "-c", "cd App && alembic upgrade head && exec uvicorn App.main:app --host 0.0.0.0 --port 8000"]