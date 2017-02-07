#!/usr/bin/env python3

import markovify as markov

with open("./texts_all.txt") as f:
    text = f.read()

text_model = markov.Text(text)
for i in range(5):
    print(text_model.make_sentence() + '\n')

for i in range(3):
    print(text_model.make_short_sentence(140) + '\n')
