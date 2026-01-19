from fastapi import APIRouter, HTTPException
from app.models.playlist import Playlist

router = APIRouter()

@router.post("/")
async def create_playlist(playlist: Playlist):
    await playlist.insert()
    return {"id": str(playlist.id)}

@router.get("/")
async def list_playlists():
    return await Playlist.find_all().to_list()

@router.get("/{playlist_id}")
async def get_playlist(playlist_id: str):
    playlist = await Playlist.find_by_id(playlist_id)
    if not playlist:
        raise HTTPException(status_code=404, detail="Playlist not found")
    return playlist