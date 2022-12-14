import base64
import aioredis
import aiohttp
from core.config import Settings, get_settings
from fastapi import Depends

from core.const import (
    ACCESS_TOKEN,
    EXPIRES_IN,
    SPOTIFY_TOKEN,
    SPOTIFY_TOKEN_URL,
)


class SpotifyAuth:
    def __init__(self, settings: Settings = Depends(get_settings)) -> None:
        self.__client_id = settings.SPOTYFI_CLIENT_ID
        self.__secret_key = settings.SPOTYFI_SECRET_KEY
        self.__redis = aioredis.from_url(f"redis://{settings.redis_url}")

    @property
    async def token(self):
        spotify_token: bytes | None = await self.__redis.get(SPOTIFY_TOKEN)
        if not spotify_token:
            spotify_token = await self.__update_token()
        return spotify_token

    async def __create_token(self) -> dict:
        auth_header = base64.urlsafe_b64encode(
            (self.__client_id + ":" + self.__secret_key).encode()
        )
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic %s" % auth_header.decode("ascii"),
        }
        payload = {"grant_type": "client_credentials"}

        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=SPOTIFY_TOKEN_URL, data=payload, headers=headers
            ) as response:
                response.raise_for_status()  # TODO: raise exception
                return await response.json()

    async def __update_token(self) -> str:
        token_data = await self.__create_token()
        await self.__redis.setex(
            SPOTIFY_TOKEN, token_data[EXPIRES_IN], token_data[ACCESS_TOKEN]
        )
        return token_data[ACCESS_TOKEN]
