from fastapi import APIRouter
from api.spotify import spotify


router = APIRouter()
router.include_router(spotify.router)
