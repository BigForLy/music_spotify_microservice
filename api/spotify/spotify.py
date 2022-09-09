from fastapi import APIRouter, Depends
from .models import SpotifyAuthModel
from services.spotify_integration.spotify_auth import SpotifyAuth
from services.spotify_integration.spotify import MySpotify


router = APIRouter()


@router.get("/v1/albums/{album_id}/track/")
async def t(album_id: str):
    return {"album_id": album_id}


@router.get("/v1/new_releases/")
async def new_releases(
    spotify_auth: MySpotify = Depends(),
):
    return await spotify_auth.get_new_releases()


@router.get("/v1/subreleases/{pk}")
async def subreleases(
    pk: str,
    spotify_auth: MySpotify = Depends(),
):
    return await spotify_auth.get_subreleases(pk)


@router.get("/info/", response_model=SpotifyAuthModel)
async def info(
    spotify_auth: SpotifyAuth = Depends(),
):
    return SpotifyAuthModel(token=await spotify_auth.token)
