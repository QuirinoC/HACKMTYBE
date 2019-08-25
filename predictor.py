LABELS = ["cancer", "measles", "hives", "cancer2", "varicella"]

from random import randint, random

import torch
import torch.nn as nn
from torch.nn import Sequential, Linear, ReLU,Dropout
from torchvision import models
from io import BytesIO
import numpy
from matplotlib.image import imread
import PIL.Image
from torch.nn import functional

from PIL import Image

resnet50 = models.resnet50()
classifier = Sequential(
        Linear(2048, 1024, bias=True),
        ReLU(inplace=True),
        Dropout(p=0.5),
        Linear(1024,512, bias=True),
        ReLU(inplace=True),
        Dropout(p=0.5),
        Linear(512, 6, bias=True)
        )

resnet50.fc = classifier

resnet50.load_state_dict(torch.load('resnet50.pt',map_location=torch.device('cpu')))
resnet50.eval()

classes = [
    'Acne',
    'Atopic',
    'Basal',
    'Hieves',
    'Melanoma',
    'Psoriasis'
]

def predict(img: "path") -> (str, float):
    
    rgba_image = PIL.Image.open(img)
    rgb_image = rgba_image.convert('RGB')
    img = numpy.array(rgb_image)
    img.resize(1,3,224,224)
   
    tensor = torch.from_numpy(img).float()
    tensor.cpu()
    resnet50.cpu()

    out = resnet50(tensor)

    _, pred = torch.max(out, 1)

    print(int(pred))

    '''print(pred[0][1])

    d =  functional.softmax(pred,dim=1).data[0]
    
    arr = numpy.array(d).reshape(6)

    label = ""

    for i, val in arr:
        if val:
            label = classes[i]'''

    return classes[pred],int(_)