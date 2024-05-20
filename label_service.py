from models import Label
import numpy as np
from keras.preprocessing import image
from keras.models import load_model
from io import BytesIO
from constant import img_width, img_height, classes, model_resnet, model_no_resnet


def get_all_labels():
    return Label.query.all()


def predict_no_resnet(image_file):
    modelLoad = load_model(model_no_resnet)
    return predict(modelLoad, image_file)


def predict_resnet(image_file):
    modelLoad = load_model(model_resnet)
    return predict(modelLoad, image_file)


def predict(modelLoad, image_file):
    img = image.load_img(BytesIO(image_file.read()),
                         target_size=(img_width, img_height))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.
    predictions = modelLoad.predict(img_array)
    predicted_class = np.argmax(predictions)
    result = classes[predicted_class]
    return result
