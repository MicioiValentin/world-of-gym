from fastapi import FastAPI

# Import routers explicitly from each submodule (avoids any package ambiguity)
from .routes.health import router as health_router
from .routes.meta import router as meta_router
from .routes.users import router as users_router
from .routes.sets import router as sets_router
from .routes.leaderboard import router as leaderboard_router

app = FastAPI(title="World of Gym API", version="0.1.0")

# Register routers
app.include_router(health_router)
app.include_router(meta_router, prefix="/v1")
app.include_router(users_router, prefix="/v1")
app.include_router(sets_router, prefix="/v1")
app.include_router(leaderboard_router, prefix="/v1")

# Optional: simple root to confirm app loaded
@app.get("/")
def root():
    return {"message": "World of Gym API is running"}
