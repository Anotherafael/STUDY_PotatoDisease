from io import BytesIO

import numpy as np
import tensorflow as tf
import uvicorn
from fastapi import FastAPI, File, UploadFile
from PIL import Image

app = FastAPI()

MODEL = tf.keras.models.load_model("../models/1.keras")
CLASS_NAMES = ["Early Blight", "Healthy", "Late Blight"]


def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


@app.post("/predict")
async def predict(
    file: UploadFile = File(...),
):
    img = read_file_as_image(await file.read())
    img_batch = np.expand_dims(img, 0)

    prediction = MODEL.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(prediction[0])]
    confidence = np.max(prediction[0])

    return {
        "class": predicted_class,
        "confidence": float(confidence),
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
