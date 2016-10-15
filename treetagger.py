##Treetagger##

import os

treetagger_german = "tree-tagger-german"
text_file = "texte-file.txt"
tagged_text_file = "tagged-text.txt"

tree_call = treetagger_german + " " + text_file + " > " + tagged_text_file
os.system(tree_call)

