import os
import sys
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Импорты роутеров
from App.Routers import user_router, product_router, order_router

# Загружаем переменные окружения
load_dotenv()

# Добавляем родительскую директорию в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Создаем приложение FastAPI
app = FastAPI(title="Shop API", version="1.0.0", docs_url="/setdocs", redoc_url=None, openapi_url="/setdocs-json")

# Настраиваем CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене укажите конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Настраиваем путь к media файлам
if "DOCKER" in os.environ:
    # Если запущено внутри Docker
    media_path = "/app/App/media"
else:
    # Локальная разработка
    current_dir = Path(__file__).parent  # App/
    media_path = current_dir / "media"

# Создаем папку, если её нет
os.makedirs(media_path, exist_ok=True)

# Монтируем статические файлы
app.mount("/media", StaticFiles(directory=str(media_path)), name="media")

# Подключаем роутеры
app.include_router(user_router.router, prefix="/api")
app.include_router(product_router.router, prefix="/api")
app.include_router(order_router.router, prefix="/api")
