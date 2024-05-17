from io import BytesIO

import numpy as np
import requests
import tensorflow as tf
import uvicorn
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    #     "http://localhost",
    #     "http://localhost:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# specific_version = "http://tensorflow:8502/v1/models/potatoes_model/versions/1:predict"
endpoint = "http://tensorflow:8502/v1/models/potatoes_model:predict"

CLASS_NAMES = ["Early Blight", "Healthy", "Late Blight"]


def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


@app.get("/ping")
async def ping():
    return {"ping": "pong"}


@app.post("/predict")
async def predict(
    file: UploadFile = File(...),
):
    img = read_file_as_image(await file.read())
    img_batch = np.expand_dims(img, 0)

    json_data = {
        "instances": img_batch.tolist(),
    }
    response = requests.post(endpoint, json=json_data)

    prediction = np.array(response.json()["predictions"][0])

    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = np.max(prediction)

    return {
        "class": predicted_class,
        "confidence": float(confidence),
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
