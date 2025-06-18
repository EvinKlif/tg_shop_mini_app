import os
import uuid
from pathlib import Path
from fastapi import HTTPException, UploadFile

# Путь к папке media в корне проекта
BASE_DIR = Path(__file__).parent.parent
MEDIA_DIR = BASE_DIR / "media"
os.makedirs(MEDIA_DIR, exist_ok=True)


async def save_photo(file: UploadFile) -> str:
    file_extension = file.filename.split(".")[-1]
    unique_filename = f"{uuid.uuid4()}.{file_extension}"
    file_path = MEDIA_DIR / unique_filename

    try:
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        return f"{unique_filename}"
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not save file: {e}")