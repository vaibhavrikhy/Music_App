
from beanie import Document
from datetime import datetime
from typing import List

class Playlist(Document):
    owner_id: str
    name: str
    track_ids: List[str] = []
    is_public: bool = True
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()

    class Settings:
        name = "playlists"
