FROM python:3.11-slim

WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код (но НЕ копируем .env здесь!)
COPY bot.py .

# Запускаем от непривилегированного пользователя
RUN useradd -m botuser && chown -R botuser:botuser /app
USER botuser

CMD ["python", "bot.py"]