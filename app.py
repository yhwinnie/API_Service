#!/usr/bin/env python
from flask import Flask, render_template
import re
import random
import markov
import os

tokens = markov.read(open("corpus_clean.txt").read())
#print(tokens)
sentence = markov.markov_model(tokens)

app = Flask(__name__)

@app.route('/')
def main():
    sentence = markov.markov_model(tokens)
    #return ' '.join(sentence).replace(" ENDEND", '.')
    img_arr = ["https://espnfivethirtyeight.files.wordpress.com/2016/08/ap_16228136310156.jpg?quality=90&strip=all&w=575&ssl=1",
    "http://cdn.history.com/sites/2/2013/11/obama_color.jpg","http://c7.nrostatic.com/sites/default/files/styles/original_image_with_cropping/public/uploaded/obama-lies-voter-id-many-countries-require-it.jpg?itok=IiyEm-f8",
    "http://www.dailystormer.com/wp-content/uploads/2016/11/obama.jpg",
    "http://www.fanabc.com/afanoromo/media/k2/items/cache/6d61dddd32fa4e7706fff4ee75eccb24_XL.jpg?t=1437743475",
    "http://i2.cdn.cnn.com/cnnnext/dam/assets/161020125737-06-obama-presidency-super-169.jpg"]


    img = random.choice(img_arr)
    print(img)

    return render_template("test.html", sentence=' '.join(sentence).replace(" ENDEND", '.'), img_src=img)

@app.route('/hello')
def hello():

    return render_template("test.html", sentence=random_sentence, img_src=img)


if __name__ == '__main__':
    import sys
    app.static_folder = 'static'
    app.run(debug=True, host='0.0.0.0')
