from tensorflow.keras.models import load_model
from pickle import load
import numpy as np
import matplotlib.pyplot as plt
from keras.models import model_from_json
import pickle

MODEL_WEIGHT_PATH = 'LeNet/model.h5'
MODEL_PATH = 'LeNet/model.json'
CLASS_LABEL_PATH = 'LeNet/labels.pickle'

def make_prediction(image):
    
    # Model JSON
    json_file = open(MODEL_PATH, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    
    loaded_model = model_from_json(loaded_model_json)
    
    # load weights into new model
    loaded_model.load_weights(MODEL_WEIGHT_PATH)
    
    print("Loaded model from disk")

    # load class labels
    file_to_read = open(CLASS_LABEL_PATH, "rb")
    labels = pickle.load(file_to_read)

    y_pred = loaded_model.predict(image)

    class_label = labels[np.argmax(y_pred)]

    return class_label