from io import BytesIO

import numpy as np
import requests
import tensorflow as tf
import uvicorn
from fastapi import FastAPI, File, UploadFile
from PIL import Image

app = FastAPI()

# specific_version = "http://localhost:8502/v1/models/potatoes_model/versions/1:predict"
endpoint = "http://localhost:8502/v1/models/potatoes_model:predict"

# MODEL = tf.keras.models.load_model("../models/1.keras")
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]


def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


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
    confidence = np.max(prediction[0])

    return {
        "class": predicted_class,
        "confidence": float(confidence),
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
