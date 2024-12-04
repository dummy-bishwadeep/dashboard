
from fastapi import APIRouter
from scripts.core.constants.api import DefaultAPI
from scripts.core.handlers.defaults import DefaultHandler
from scripts.logging.logging import logger

default_router = APIRouter(prefix=DefaultAPI.prefix)
handler = DefaultHandler


@default_router.get(DefaultAPI.load_styles)
async def load_styles():
    """
    Default: Loads required endpoints to get filenames in the build
    Do not edit this
    """
    return handler.load_styles()


@default_router.get(DefaultAPI.load_file)
def download_resource(filename: str):
    """Default: Request Build Files to redner widget configurations on the frontend
    Do not edit this
    """
    return handler.download_resources(filename)


# TODO: Add preview logic. Do not change the API endpoint



@default_router.get(DefaultAPI.load_configuration)
async def load_configuration():
    """
    Default: Load widget configuration JSON for listing plugins while creating widgets
    Do not edit this
    """
    return handler.load_configuration()

