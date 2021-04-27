#!/usr/bin/env python3

from nltk.util import trigrams
import random


def is_first_key(string):
    """Return if a key bigrams can be placed in the beginning of the sentence."""

    string = string[0].split()

    return string[0].istitle() and not string[0].endswith(".") and not string[0].endswith("!") and not \
        string[0].endswith("?") and not string[0].startswith('"') and not string[1].endswith(".") and not \
        string[1].endswith("!") and not string[1].endswith("?") and not string[0].startswith('[') and not \
        string[0].startswith('[')("“")


def is_first_word(string):
    """Return if a word can be placed in the beginning of the sentence."""

    return string.istitle() and not string.endswith(".") and not string.endswith("!") and not string.endswith("?") and not string.startswith('"')


def is_final_key(string):
    """Return if a key bigrams can be placed at the end of the sentence."""

    string = string[0].split()
    return string[1].endswith(".") or string[1].endswith("!") or string[1].endswith("?") or string[1].endswith(',')


def is_final_word(string):
    """Return if a word can be placed at the end of the sentence."""

    return string.endswith(".") or string.endswith("!") or string.endswith("?")


text = input()
words = []
ngrams = {}
with open(text, 'r', encoding='utf-8') as corpus:
    for row in corpus:
        for word in row.split():
            words.append(word)

words_ngrams = list(trigrams(words))

for gram in words_ngrams:
    head = gram[0] + " " + gram[1]
    tail = gram[2]
    if head not in ngrams:
        ngrams[head] = {tail: 1}
    else:
        if tail in ngrams[head]:
            ngrams[head][tail] += 1
        else:
            ngrams[head][tail] = 1


for i in range(10):
    sentence = ""
    first_word = random.choices([key for key in ngrams.keys() if is_first_key([key])])
    sentence = sentence.join(first_word)
    count_word = 2
    next_word = ["stop"]
    while not is_final_word(next_word[0]) or count_word < 5:
        try:
            next_word = random.choices([key for key in ngrams[first_word[0]].keys()], [int(value) for value in ngrams[first_word[0]].values()])
        except KeyError:
            next_word = random.choices([key for key in ngrams.keys()])
        sentence = sentence + " " + next_word[0]
        count_word += 1
        first_word = [sentence.split()[-2] + " " + sentence.split()[-1]]

    print(sentence)
