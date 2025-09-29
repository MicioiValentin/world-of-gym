from contextlib import asynccontextmanager
from fastapi import FastAPI
from .db import init_db

async def lifespan(app: FastAPI):
    init_db()
    yield