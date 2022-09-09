from pydantic import BaseModel


class SpotifyAuthModel(BaseModel):
    token: str
