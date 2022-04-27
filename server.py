import numpy as np
import pandas as pd 
import tensorflow as tf

from datetime import date as d
from tensorflow import keras
from tensorflow.keras.models import load_model
from keras_preprocessing import image
from flask import Flask, jsonify, request


SERVER_INFO = {
    'AUTHOR': '\nRebecca Norwood',
    'NAME': '\nRock, Paper, Scissors image classification server.',
    'CURRENT_DATE_TIME': '\n' + d.today().strftime("%B %d, %Y")
}

MODEL_PATH = 'Z:/School/CSUSM/Spring 2022/CS 478/Assignments/Norwood_Assignment6/model.h5'
IMAGE_FILE_PATH = 'Z:/School/CSUSM/Spring 2022/CS 478/Assignments/Norwood_Assignment6/client_images/'


# initialize our Flask application
app = Flask(__name__)

#load the model
MODEL_PATH = 'Z:/School/CSUSM/Spring 2022/CS 478/Assignments/Norwood_Assignment6/model.h5'
model = load_model(MODEL_PATH)


@app.route('/', methods=['GET'])
def index():
    return (SERVER_INFO['NAME'] + 
            SERVER_INFO['AUTHOR'] + 
            SERVER_INFO['CURRENT_DATE_TIME'])


"""Test the model with test images"""
"""here are some images located at: https://oreil.ly/dEUpx"""

@app.route('/predict', methods=['GET', 'POST'])
def predict():

    classifcation = ['paper', 'rock', 'scissors']
    
    if request.method == 'POST':
        posted_data = request.get_json()
        data = posted_data['data']

        image_param = IMAGE_FILE_PATH + data
        img = image.load_img(image_param, target_size=(150,150))

        x = image.img_to_array(img)
        x = np.expand_dims(x, axis = 0)

        images = np.vstack([x])
        classes = model.predict(images, batch_size = 10)
        print(classes)

        #Iterate through numpy array of images and set proper category dependent on array position
        for outerloop in classes:
            for idx, num in enumerate(outerloop):
                if num == 0:
                    continue
                else:
                    category = classifcation[idx]
                    print(category)


    return jsonify(str("The image you've submitted is classified as a: " + str(category)))


#  main thread of execution to start the server
if __name__=='__main__':
    app.run(debug=True)