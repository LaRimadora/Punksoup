## analyse punk-texts ##

# finding constructions of adjectives and nouns #

adja_nn_list = []

preitem = ["test", "test"]

# tokens_tagged_list im treetagger-script #

for item in tokens_tagged_list:
    if item[1] == 'NN':
        if preitem[1] == 'ADJA':
            word = preitem[0] + " " + item[0]
            adja_nn_list.append(word)
    preitem = item

print(adja_nn_list)

#with open(AD, 'w') as f:
 #   f.write("\n".join(adja_nn_list))

# concordance #


