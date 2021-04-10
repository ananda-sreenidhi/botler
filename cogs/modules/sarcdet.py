import re
import pickle
import os

import warnings
warnings.filterwarnings("ignore")

path = os.getcwd()
x = open("cogs/modules/model.pickle", "rb")
mp = pickle.load(x)
x.close()
y = open("cogs/modules/vect.pickle", "rb")
vp = pickle.load(y)
y.close()
z = open("cogs/modules/tfidf.pickle", "rb")
tp = pickle.load(z)
z.close()

def predict(text):
    text = tp.transform(vp.transform([text]))
    return "Sarcastic." if mp.predict(text)[0] == 1 else "Serious."