DATABASE_URI = 'postgresql://postgres:123456@localhost/Label'

SQLALCHEMY_TRACK_MODIFICATIONS = False

img_width, img_height = 224, 224

classes = ["Anthracnose",  "Bacterial Canker",  "Cutting Weevil",  "Die Back",  "Gall Midge",
           "Healthy",  "Powdery Mildew",  "Sooty Mould", ]

model_resnet = "resnet_model_224_70_open_checkpoint_1_10.h5"

model_no_resnet = "no_resnet_model_224_3_checkpoint_1_10.h5"
