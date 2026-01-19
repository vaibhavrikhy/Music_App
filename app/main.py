from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings
from app.models.user import User
from app.models.track import Track
from app.models.playlist import Playlist
from app.routers import auth, tracks, playlists

app = FastAPI(title="Music app", version="0.1.0")

@app.on_event("startup")
async def on_startup():

    client = AsyncIOMotorClient(settings.MONGODB_URI)
    db = client.get_default_database()
    await init_beanie( database=db,
                       document_models=[User, Track, Playlist],
                       )

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(tracks.router, prefix="/tracks", tags=["tracks"])
app.include_router(playlists.router, prefix="/playlists", tags=["playlists"])

