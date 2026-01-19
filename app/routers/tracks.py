from fastapi import APIRouter, HTTPException
from app.models.track import Track

router = APIRouter()

@router.post("/")
async def create_track(track: Track):
    await track.insert()
    return {"id": str(track.id)}

@router.get("/")
async def list_tracks():
    return await Track.find_all().to_list()

@router.get("/{track_id}")
async def list_tracks():
    return await Track.find_all().to_list()

@router.get("/{track_id}")
async def get_track(track_id: str):
    track = await Track.get(track_id)
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")
    return track
@router.delete("/{track_id}")
async def delete_track(track_id: str):
    track = await Track.get(track_id)
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")
    await track.delete()
    return {"ok": True}