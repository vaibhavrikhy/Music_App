from beanie import Document, Indexed
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class AudioFeatures(BaseModel):
    bpm: Optional[int] = None
    energy: Optional[float] = None
    danceability: Optional[float] = None
    valence: Optional[float] = None
    key: Optional[int] = None
    mode: Optional[int] = None


class Track(Document):
    # We’ll keep title indexed (normal index), not text index for now
    title: Indexed(str)  # type: ignore
    artists: List[str] = []
    album: Optional[str] = None
    duration_ms: Optional[int] = None
    genres: List[str] = []
    year: Optional[int] = None
    audio_features: Optional[AudioFeatures] = None
    created_at: datetime = datetime.utcnow()

    class Settings:
        name = "tracks"
