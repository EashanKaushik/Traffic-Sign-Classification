from flask import url_for, render_template, Flask, request
from deploy.utils import make_prediction
from tensorflow.keras.preprocessing import image
import numpy as np

def home():
    file_upload = False
    if request.method == 'POST':
        file_upload = True

        imgfile = request.files['imgfile']

        imgfile.save('static/images/upload.JPG')

        img = image.load_img('static/images/upload.JPG', target_size=(32, 32))
        img = np.array(img)
        img = np.expand_dims(img, axis=0)
        img = np.sum(img/3, axis=3, keepdims=True)
        img = (img - 128)/128

        class_label = make_prediction(img)
        
        data = {
            'class_label': class_label
        }

        return render_template('home.html', pagename='Traffic Sign Classification', file_upload=file_upload, data=data)
    
    return render_template('home.html', pagename='Traffic Sign Classification', file_upload=file_upload)