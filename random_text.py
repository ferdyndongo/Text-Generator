#!/usr/bin/env python3

from nltk.util import bigrams
import random

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

sentence = ""
max_length_sentence = 10
first_word = random.choice(words)

for i in range(10):
    sentence = sentence.join(first_word)
    count_word = 1
    while count_word < max_length_sentence:
        try:
            random.choices([key for key in ngrams[first_word[0]].keys()], [int(value) for value in ngrams[first_word[0]].values()])
        except KeyError:
            break
        else:
            next_word = random.choices([key for key in ngrams[first_word[0]].keys()], [int(value) for value in ngrams[first_word[0]].values()])
        sentence = sentence + " " + next_word[0]
        first_word = next_word
        count_word += 1
    print(sentence)
    sentence = ""
