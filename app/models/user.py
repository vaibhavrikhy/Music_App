from beanie import Document, Indexed
from datetime import datetime
from passlib.context import CryptContext

pws_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Document):
    email: Indexed(str, unique=True)
    hashed_password: str
    display_name: str | None = None
    liked_tracks_ids: list[str] = []
    created_at: datetime = datetime.utcnow()

    class Settings:
        name = "users"

    def verify_password(self,raw: str) -> bool:
        return pws_ctx.verify(raw, self.hashed_password)
    @staticmethod
    def hash_password(raw: str) -> str:
        return pws_ctx.hash(raw)