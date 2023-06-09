from flask import Flask, request, jsonify,render_template

import tensorflow as tf

import numpy as np
import time
import cv2
import os


print(os.listdir('ecom Images'))
class_names = ['Baby and Kids', 'Excercise and Fitness', 'Food Essentials', 'Footwear', 'Furnitures', 'Home and Kitchen Appliances', 'Mens fashion', 'New folder', 'Sports', 'Stationery', 'Womens fashion', 'electronics', 'mobiles and laptops']
app = Flask(__name__)
@app.route('/',methods=['post','get'])
def homepage():
    return render_template('index.html')

model = tf.keras.models.load_model('productPrediction.h5')

@app.route('/predict', methods=['POST'])
def Prediction():
    img_path = request.files['image'].read()

    file_bytes = np.fromstring(img_path, np.uint8)
    img_path = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)

    img = cv2.resize(img_path, (224, 224))
    img_array = np.expand_dims(img, axis=0)
    image = np.array(img_array) / 255.0
    input_data = np.array(image, dtype=np.float32)
    start_time = time.time()
    prediction = model.predict(input_data)
    print(prediction)
    end_time = time.time()
    output_data = prediction[0]
    prediction = np.argmax(output_data)
    prediction = class_names[prediction]
    inference_time = end_time - start_time

    return render_template('results.html', prediction=(prediction,'inference time: ',inference_time))


if __name__ == '__main__':
    app.run(debug=True)