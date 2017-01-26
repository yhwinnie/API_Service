#!/usr/bin/env python
from flask import Flask, render_template
import re
import random
import markov
import os

tokens = markov.read(open("corpus_clean.txt").read())
print(tokens)
sentence = markov.markov_model(tokens)

app = Flask(__name__)

@app.route('/')
def main():
    sentence = markov.markov_model(tokens)
    #return ' '.join(sentence).replace(" ENDEND", '.')
    return render_template("test.html", sentence=' '.join(sentence).replace(" ENDEND", '.'))

@app.route('/hello')
def hello():
    return render_template("test.html", sentence=random_sentence)


if __name__ == '__main__':
    import sys
    #main()
    app.run(debug=True, host='0.0.0.0')
