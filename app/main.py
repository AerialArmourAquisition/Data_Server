import os
import pathlib
import uuid
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/image/")
async def upload_image(file: UploadFile = File(...)):
    file.filename = f"{uuid.uuid4()}.jpg"
    image = await file.read()

    with open(file.filename, "wb") as f:
        f.write(image)

    return {"filename": file.filename}


@app.get("/image/")
async def download_image(name: str):
    if not os.path.exists(name):
        return {"message": "File Not Found"}, 404

    path = pathlib.Path().absolute()
    path = str(path) + f"/{name}"
    return FileResponse(path)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
