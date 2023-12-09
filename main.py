import os
import cv2
import keras
import numpy as np
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

app.config['DEBUG'] = os.getenv("FLASK_DEBUG")
model = keras.models.load_model('ecobin_model.h5')
CLASSES = ["biodegradable", "cardboard", "glass", "metal", "paper", "plastic"]
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']


def preprocess_image(bytes):
    image_data = bytes
    image = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)
    image = cv2.resize(image, (256, 256))
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image


def predict(image):
    predictions = {}
    model_predictions = model.predict(image)[0]
    for i in range(len(model_predictions)):
        predictions[CLASSES[i]] = float(model_predictions[i])
    predictions = dict(sorted(predictions.items(), key=lambda item: item[1], reverse=True))
    sorted_predictions = []
    for key, value in predictions.items():
        sorted_predictions.append({key: value})
    return sorted_predictions


@app.get("/")
def index():
    return "halo dunia real"


@app.get("/api")
def api():
    if 'image' not in request.files:
        return jsonify({'message': 'No image file sent'}), 400
    image = request.files['image']
    if image.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    if (
            '.' not in image.filename
            or image.filename.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS
    ):
        return jsonify({'message': 'Invalid file format', 'ALLOWED_EXTENSIONS': ALLOWED_EXTENSIONS}), 400
    try:
        image = preprocess_image(image.read())
        if image is None:
            raise TypeError()
    except:
        return jsonify({'message': 'Error reading or decoding the image'}), 500
    predictions = predict(image)
    return jsonify({'predictions': predictions}), 200

if __name__ == '__main__':
    port = int(os.getenv('FLASK_PORT'))
    app.run(host='0.0.0.0', port=port)