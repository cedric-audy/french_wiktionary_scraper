from WiktionaryParser.wiktionaryparser import WiktionaryParser
import sys
import random

path_list = './french_words/liste_francais.txt'
path_defs = './french_words/definitions_fr.txt'

word_file = open(path_list, 'r', encoding="utf-8")
defined_words = open(path_defs, 'w+',encoding="utf-8")
word_arr = word_file.read().splitlines()

parser = WiktionaryParser()
i = 1000
entries = []
for w in range(i):
    word = word_arr[random.randint(0,len(word_arr))]
    try:
        word_and_def = parser.fetch(word,'français')
        #print(word_and_def)
        test = word_and_def[0].get('definitions')[1].get('text')[1]
        test_ety = word_and_def[0].get('etymology')
        print(test_ety)
        print()
        '''  defline = word + " & " + test
        defline = defline.lower()
        defline.replace('&', 'amp')
        defline += '\n'
        print(defline)
        defined_words.write(defline)'''
    except KeyboardInterrupt:
        break
    except:
        pass

try:
    pass
finally:
    word_file.close()
    defined_words.close()