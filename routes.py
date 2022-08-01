from fastapi import APIRouter
from spotify import spotify


router = APIRouter()
router.include_router(spotify.router)
