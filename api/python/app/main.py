from app.routes import metrics, profiles
from fastapi import FastAPI

from .lifespan import lifespan
from .routes.health import router as health_router
from .routes.leaderboard import router as leaderboard_router
from .routes.meta import router as meta_router
from .routes.sets import router as sets_router
from .routes.users import router as users_router

app = FastAPI(title="World of Gym API", version="0.1.0", lifespan=lifespan)

app.include_router(metrics.router)
app.include_router(profiles.router)
app.include_router(health_router)
app.include_router(meta_router, prefix="/v1")
app.include_router(users_router, prefix="/v1")
app.include_router(sets_router, prefix="/v1")
app.include_router(leaderboard_router, prefix="/v1")


@app.get("/")
def root():
    return {"message": "World of Gym API is running"}


@app.get("/healthz", tags=["infra"])
def healthz():
    return {"status": "ok"}
