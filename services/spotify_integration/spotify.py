from .spotify_auth import SpotifyAuth
import aiohttp
from aiohttp_socks import ProxyConnector
from core.config import Settings, get_settings
from fastapi import Depends


class MySpotify(SpotifyAuth):
    def __init__(self, settings: Settings = Depends(get_settings)) -> None:
        super().__init__(settings)
        self.proxy_url = settings.proxy_url

    async def get_new_releases(self) -> dict:
        url = "https://api.spotify.com/v1/browse/new-releases?limit=50"
        return await self._get_new_releases(url)

    async def _get_new_releases(self, url) -> dict:
        response_json = await self.__requests(url)
        result = response_json.get("albums").get("items")
        if response_json.get("albums").get("next"):
            result += await self._get_new_releases(
                response_json.get("albums").get("next")
            )
        return result

    async def get_subreleases(
        self, parent_pk
    ) -> dict:  # TODO: get_album_tracks deprecated
        url = f"https://api.spotify.com/v1/albums/{parent_pk}"
        response_json = await self.__requests(url)
        return response_json.get("tracks").get("items")

    # def get_info_about_song(self, url) -> Song:
    #     response_json = self.__requests(url)
    #     return Song(
    #         response_json['name'],
    #         response_json['artists'][0]['name'],
    #         response_json['duration_ms'],
    #         ""
    #     )

    async def __requests(self, url) -> dict:
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer %s" % await self.token,
        }
        connector = ProxyConnector.from_url(self.proxy_url)
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get(url, headers=headers) as response:
                return await response.json()
