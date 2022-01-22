import os
import pathlib
import uuid
import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/image/", status_code=201)
async def upload_image(file: UploadFile = File(...)):

    filename = f"{uuid.uuid4()}.jpg"

    path = pathlib.Path().absolute()
    path = str(path) + f"/images/{filename}"

    image = await file.read()

    with open(path, "wb") as file:
        file.write(image)

    return {"filename": filename}


@app.get("/image/", status_code=200)
async def download_image(name: str):

    path = pathlib.Path().absolute()
    path = str(path) + f"/images/{name}"

    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Item not found")

    return FileResponse(path)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
