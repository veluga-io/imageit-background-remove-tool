from pathlib import Path

import uvicorn
import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(__dir__)
sys.path.append(os.path.abspath(os.path.join(__dir__, '../../')))

from carvekit import version
from carvekit.web.deps import config
from carvekit.web.routers.api_router import api_router

app = FastAPI(title="CarveKit Web API", version=version)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")
app.mount(
    "/",
    StaticFiles(directory=Path(__file__).parent.joinpath("static"), html=True),
    name="static",
)

if __name__ == "__main__":
    uvicorn.run(app, host=config.host, port=config.port)
