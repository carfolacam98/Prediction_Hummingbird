from flask import Flask, request, jsonify, render_template
from preprocess import predict_with_labels
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    img_path = 'temp_image.jpg'
    file.save(img_path)

    try:
        predicted_label, probability = predict_with_labels(img_path)
        return jsonify({'label': predicted_label, 'probability': float(probability)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        os.remove(img_path)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

