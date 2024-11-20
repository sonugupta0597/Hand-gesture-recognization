from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import tensorflow as tf
from cvzone.ClassificationModule import Classifier

app = Flask(__name__)

# Load the pre-trained model and class names
classifier = Classifier("model5.h5", "hello.txt")
className = [
    "Good Bye",
"Good Luck",
"Hello",
"I Love You",
"Losers",
"Ok",
"Silent",
"Sorry",
"Stop",
"Victory",
]
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        # Read the image
        img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        
        # Preprocess the image
        imgWhite = np.ones((300, 300, 3), np.uint8) * 255
        imgResize = cv2.resize(img, (300, 300))
        imgWhite[:300, :] = imgResize
        
        # Get the prediction
        prediction, index = classifier.getPrediction(imgWhite, draw=False)
        print("Prediction ",prediction,"Index ",index,"Classifier ",className[index])
        result =  jsonify({'prediction': className[index] })
        print(result)
        return result

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
