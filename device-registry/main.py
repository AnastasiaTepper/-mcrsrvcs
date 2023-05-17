import uvicorn
import pickle
import logging
import requests
from fastapi import FastAPI, Request
from typing import Union, Optional
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from common.configs.conf import values as config
from common.utils.exceptions import ServerException


devices = {}
app = FastAPI()


class Device(BaseModel):
    name: str
    id: int


@app.post("/device/register")
def register_device(device: Device):
    devices[device.id] = device
    return JSONResponse(
        status_code=200,
        content={"success": True},
    )


@app.get("/devices/")
def get_all_devices():
    return JSONResponse(
        status_code=200,
        content=jsonable_encoder(devices),
    )


@app.exception_handler(ServerException)
async def server_exception_handler(request: Request, exc: ServerException):
    logging.error(exc.name)
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.name, "success": False},
    )


if __name__ == '__main__':
    uvicorn.run("main:app", port=3770, reload=False)