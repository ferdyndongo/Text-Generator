#!/usr/bin/env python3


from nltk.probability import FreqDist

text = input()
words = []
with open(text, 'r', encoding='utf-8') as corpus:
    for row in corpus:
        for word in row.split():
            words.append(word)
words_stat = FreqDist(words)
print(f"""Corpus statistics
All tokens: {len(words)}
Unique tokens: {len(words_stat)}
""")
index = input()
while index != "exit":
    try:
        int(index)
    except TypeError:
        print("Type Error. Please input an integer.")
    except ValueError:
        print("Type Error. Please input an integer.")
    else:
        try:
            words[int(index)]
        except IndexError:
            print("Index Error. Please input an integer that is in the range of the corpus.")
        else:
            print(words[int(index)])
    index = input()
