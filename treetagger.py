##Treetagger##

## Treetagger muss manuell installiert werden:
## http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/

import os
import re

## Pfad für treetagger-Datei im Programm-Ordner angeben:

treetagger_german = "/home/larimadora/Programme/TreeTagger/tree-tagger-german"
text_file = "texte-file.txt"
tagged_text_file = "tagged-text.txt"

tree_call = treetagger_german + " " + text_file + " > " + tagged_text_file
os.system(tree_call)

with open(tagged_text_file) as f:
    contents = f.readlines()

texte_tagged_list = []

for line in contents:
    texte_tagged_list.append(re.split("\t|\n", line))

tokens_tagged_list = []

## Lemma-Einträge mit <unknown> werden durch Token ersetzt:

for item in texte_tagged_list:
    if len(item) == 4:
        tokens_tagged_list.append(item[0:3])

print(tokens_tagged_list)