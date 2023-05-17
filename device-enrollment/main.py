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


app = FastAPI()


class Device(BaseModel):
    name: str
    id: int


@app.post("/device/add")
def add_device(device: Device):
    try:
        res = requests.post(config.get('registry_url'), json=jsonable_encoder(device))
        if res.status_code == 200:
            return JSONResponse(
                                status_code=200,
                                content={"success": True},
                            )
        else:
            return JSONResponse(
                status_code=res.status_code,
                content={"success": False},
            )
    except Exception as e:
        raise ServerException(str(e), status_code=500)


@app.exception_handler(ServerException)
async def server_exception_handler(request: Request, exc: ServerException):
    logging.error(exc.name)
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.name, "success": False},
    )


if __name__ == '__main__':
    uvicorn.run("main:app", port=2770, reload=False)