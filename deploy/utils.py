from tensorflow.keras.models import load_model
from pickle import load
import numpy as np
import matplotlib.pyplot as plt

# MODEL_PATH = 'model/20210720-184145.h5'
# CLASS_LABEL_PATH = 'model/cifar_label_name.pkl'

# model = load_model(MODEL_PATH)

def make_prediction(image):
    pass
    
#     class_label = load(open(CLASS_LABEL_PATH, 'rb'))

#     labels = [l.decode('utf-8') for l in class_label]

#     y_pred = model.predict(image)

#     val = dict(zip(labels, y_pred.tolist()[0]))

#     class_index = np.argmax(y_pred, axis=1)
#     class_label = class_label[class_index]
#     class_label = class_label[0].decode('utf-8')

#     color_list = ['#800000', '#e6194B', '#f58231', '#ffe119', '#bfef45', '#aaffc3', '#dcbeff', '#469990', '#9A6324', '#808000']
#     count = 0
    
#     plt.figure(figsize=(12,10))
#     barlist=plt.bar(val.keys(), val.values())
#     for barl in barlist:
#         barl.set_color(color_list[count])
#         count += 1
#     plt.grid()
#     plt.savefig('static/images/graph.jpg')

#     return class_label