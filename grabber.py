#!/usr/bin/env python3

import urllib
import urllib.request
import re
from bs4 import BeautifulSoup

#Expressions to delete
strip = {'\\n\'','\\n', '<td>', '</td>', '<tr>', '</tr>', '\\r'}

#Unicode Characters to replace, which failed to convert
ersetzen = [['\\x99', u'\x99'], ['\\xe5',u'\xef'], ['\\xd1',u'\xd1'], ['\\xcd',u'\xcd'], ['\\xc1',u'\xc1'], ['\\xc9',u'\xc9'], \
        ['\\xbd',u'\xbd'], ['\\xb2', u'\xb2'], ['\\xeb',u'\xeb'], ['\\x8a',u'\x8a'], ['\\xc7',u'\xc7'], ['\\xe7',u'\xe7'],\
        ['\\x9e',u'\x9e'], ['\\x9c',u'\x9c'], ['\\x9b',u'\x9b'], ['\\x8b',u'\x8b'], ['\\xb0',u'\xb0'], ['\\xf1',u'\xf1'],\
        ['\\xbf',u'\xbf'], ['\\xa9', u'\xa9'], ['\\xbb', u'\xbb'], ['\\xe3',u'\xe3'], ['\\xc3',u'\xc3'], ['\\xbc', u'\xbc'],\
        ['\\xf8', u'\xf8'], ['\\xe6', u'\xe6'], ['\\xed',u'\xed'], ['\\xe8',u'\xe8'], ['\\xf4', u'\xf4'], ['\\xea', u'\xea'],\
        ['\\xab',u'\xab'], ['\\xee', u'\xee'],['\\xfa', u'\xfa'], ['\\xe1', u'\xe1'], ['\\xf3', u'\xf3'], ['\\xef','ï'],\
        ['\\xa5', '¥'], ['\\xe2', 'â'], ['\\xe9', 'é'], ['\\x80', '€'], ['\\xe0', 'à'] ,['\\x96', '-'],['\\x97', '-'],\
        ['\\xad', u'\xad'], ['\\xdc','Ü'], ['\\xe4','ä'],['\\xfc','ü'], ['\\xdf', 'ß'], ['\\xfe','þ'], ['\\xd6','Ö'],\
        ['\\xf6','ö'], ['\\x92', '\''],['\\xc4', 'Ä'], ['\\\'', '\''], ['\\x84', '\"'], ['\\x94','\"'], ['\\x93', '\"'],\
        ['\\xb4','\''], ['\\x82', '\''], ['\\x91','\''], ['\\x85','...'], ['\\xb5',u'\xb5'], ['\\xa7', u'\xa7']]

def extract(url):
    urlStream = urllib.request.urlopen(url)
    textFromWeb = str(urlStream.read())
    #print(textFromWeb)
    textFromWeb = textFromWeb.replace('b\'', '', 1) #replace the first b' at the start of the page
    textFromWeb = textFromWeb.replace('<br>', '\n')

    #replace stuff in ersetzen
    for strings in ersetzen:
        textFromWeb = textFromWeb.replace(strings[0], strings[1])

    #delete expressions in strip
    for strings in strip:
        textFromWeb = textFromWeb.replace(strings, '')

    #regular expressions for removing <> html elements
    textFromWeb = re.sub('\[<.*?>.*?</.*?>\]', '', textFromWeb)
    textFromWeb = re.sub('<.*?>.*?</.*?>', '', textFromWeb)
    textFromWeb = re.sub('<.*?>', '', textFromWeb)

    #rest of overlooked html or other text
    textFromWeb = textFromWeb.replace(' oder andere Texte von :', '')
    textFromWeb = textFromWeb.replace(' --\'', '')
    #textFromWeb = textFromWeb.replace('\n', ' ')
    textFromWeb = re.sub('\s+', ' ', textFromWeb).strip() #remove excess whitespaces
    return(textFromWeb)

#print(mystring)


urlbeg = "http://jedermenschistzuviel.stabo.org/texte.php?show=2&what="

f = open('./test.txt', 'w')
for i in range(1, 8151): #set range of websites, 8151 is max.
    url = urlbeg + str(i)
    data = extract(url)
    #f = open('./data/' + str(i) + '.txt', 'w')
    f.write(data + '\n')
    
    #debug
    #if "\\x" in data:
    #    print(i)
    #print(re.match("\\x", data, i)
    



