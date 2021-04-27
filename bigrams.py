#!/usr/bin/env python3


from nltk.probability import FreqDist
from nltk import bigrams

text = input()
words = []
with open(text, 'r', encoding='utf-8') as corpus:
    for row in corpus:
        for word in row.split():
            words.append(word)
words_stat = FreqDist(words)
words_ngrams = list(bigrams(words))
print(f"Number of bigrams: {len(words_ngrams)}")
index = input()
while index != "exit":
    try:
        int(index)
    except TypeError:
        print("Typ Error. Please input an integer.")
    except ValueError:
        print("Typ Error. Please input an integer.")
    else:
        try:
            words_ngrams[int(index)]
        except IndexError:
            print("Index Error. Please input a value that is not greater than the number of all bigrams.")
        else:
            print(f"Head: {words_ngrams[int(index)][0]} Tail: {words_ngrams[int(index)][1]}")
    index = input()
