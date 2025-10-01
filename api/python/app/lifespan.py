from contextlib import asynccontextmanager
from fastapi import FastAPI

async def lifespan(app: FastAPI):
    yield