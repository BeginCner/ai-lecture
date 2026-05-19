from flask import Flask, request, jsonify
from tensorflow.keras.preprocessing import image
from tensorflow.keras import models
import numpy as np

app = Flask(__name__)
model = models.load_model('dogs-vs-cats.keras')

@app.route('/predict', methods=['POST'])
def predict():
    img_path = request.form['id']
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img).astype(float) / 255
    img_batch = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_batch)
    prediction = str(prediction.flatten()[0])

    print('prediction =>', prediction)
    
    data = {'result' : prediction}

    return jsonify(data)