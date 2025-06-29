from flask import Flask, render_template, request, redirect, send_file
from stegano_utils import encode_image, decode_image
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploaded'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    message = request.form['message']
    image_file = request.files['image']

    if not message or not image_file:
        return "Missing data!"

    path = os.path.join(UPLOAD_FOLDER, image_file.filename)
    image_file.save(path)
    output_path = os.path.join(UPLOAD_FOLDER, 'output.png')

    encode_image(path, message, output_path)
    return render_template('result.html', mode='encode', original=path, result=output_path)

@app.route('/decode', methods=['POST'])
def decode():
    image_file = request.files['image']

    if not image_file:
        return "No file uploaded"

    path = os.path.join(UPLOAD_FOLDER, image_file.filename)
    image_file.save(path)
    message = decode_image(path)
    return render_template('result.html', mode='decode', message=message, original=path)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Get PORT from environment, default to 5000
    app.run(host='0.0.0.0', port=port, debug=True)
