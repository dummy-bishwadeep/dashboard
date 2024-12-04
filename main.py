import os
from dataclasses import dataclass, field
from typing import Optional
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from scripts.config import Service
from scripts.core.constants.app_constants import Secrets
from scripts.logging.logging import logger
from scripts.utils.security_utils.jwt_signature_validator import EncodedPayloadSignatureMiddleware
from scripts.core.services.defaults import default_router

@dataclass
class FastAPIConfig:
    title: str = "Visualization Service"
    description: str = "Diageo Dashboards"
    docs_url: str = os.environ.get("SW_DOCS_URL")
    redoc_url: str = field(default=None)
    # root_path: str = os.environ.get("MODULE_PROXY", default="/d_oee")
    openapi_url: Optional[str] = os.environ.get("SW_OPENAPI_URL")


app = FastAPI(**FastAPIConfig().__dict__)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

try:
    if Service.verify_signature and Service.verify_signature in {"true", "True", True}:
        app.add_middleware(
            EncodedPayloadSignatureMiddleware,
            jwt_secret=Secrets.signature_key,
            jwt_algorithms=Secrets.alg,
            protect_hosts=Service.PROTECTED_HOSTS,
        )
except Exception as e:
    logger.error(f"Main.py file error : {str(e)}")

app.include_router(default_router)
app.mount("/assets", StaticFiles(directory=f"{Service.BUILD_DIR}/assets"), name="assets")


@app.get("/visualization/healthcheck")
async def ping():
    return {"status": 200}