from flask import Flask, request, render_template, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import werkzeug

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('ai_vs_real_model.hdf5')

# Ensure the static directory exists
if not os.path.exists('static'):
    os.makedirs('static')

def sanitize_filename(filename):
    return werkzeug.utils.secure_filename(filename)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    img = request.files['file']
    if img.filename == '':
        return jsonify({'error': 'No selected file'})

    sanitized_filename = sanitize_filename(img.filename)
    img_path = os.path.join('static', sanitized_filename)
    img.save(img_path)

    img = image.load_img(img_path, target_size=(32, 32))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0

    prediction = model.predict(img)
    pred_label = 'Real Art' if np.argmax(prediction) == 1 else 'AI Art'

    return render_template('home.html', prediction=pred_label, img_path=sanitized_filename)

if __name__ == '__main__':
    app.run(debug=True)
