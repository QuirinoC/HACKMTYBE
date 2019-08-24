LABELS = ["cancer", "measles", "hives", "cancer2", "varicella"]

from random import randint, random



def predict(img: "IMAGETYPE") -> (str, float):
    return LABELS[randint(0,len(LABELS) - 1)] , random()