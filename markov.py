#!/usr/bin/env python3

import markovify as markov

with open("./texts_all.txt") as f:
    text = f.read()

text_model = markov.Text(text)
for i in range(5):
    print(text_model.make_sentence() + '\n')

for i in range(3):
    print(text_model.make_short_sentence(140) + '\n')


# import markovify
import nltk
import re

class POSifiedText( markov.Text ):
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

posModel = POSifiedText.Text(text)
for i in range(5):
    print( posModel.make_short_sentence(100) + '\n' )