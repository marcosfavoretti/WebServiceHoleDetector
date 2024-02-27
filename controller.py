from typing import Union
from Objects.DataDto import DataDto
from service import ImageHandle
from fastapi import FastAPI
app = FastAPI()

@app.post("/")
async def readImage(data: DataDto):
    numberofholes, filename = await ImageHandle(data.x64).findHoles()
    return {"nHoles": numberofholes,
            "fileName": filename}
