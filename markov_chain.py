#!/usr/bin/env python3

from nltk.util import bigrams

text = input()
words = []
ngrams = {}
with open(text, 'r', encoding='utf-8') as corpus:
    for row in corpus:
        for word in row.split():
            words.append(word)

words_ngrams = list(bigrams(words))

for gram in words_ngrams:
    if gram[0] not in ngrams:
        tail = {gram[1]: 1}
        ngrams[gram[0]] = tail
    else:
        if gram[1] in ngrams[gram[0]]:
            ngrams[gram[0]][gram[1]] = ngrams[gram[0]][gram[1]] + 1
        else:
            ngrams[gram[0]][gram[1]] = 1

index = input()
while index != "exit":
    if index in ngrams:
        print(f"Head: {index}")
        for tail in ngrams[index]:
            print(f"Tail: {tail} Count: {ngrams[index][tail]}")
    else:
        print("The requested word is not in the model. Please input another word.")
    index = input()
