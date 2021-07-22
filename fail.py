# Для запуска сервера набрать в терминале
# uvicorn file.py:app


from fastapi import FastAPI

app = FastAPI(title="Random phrase")
