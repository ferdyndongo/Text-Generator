#!/usr/bin/env python3

from nltk.util import bigrams
import random


def is_first_word(string):
    """Return if a word can be placed in the beginning of the sentence."""

    return string.istitle() and not string.endswith(".") and not string.endswith("!") and not string.endswith("?") and not string.startswith('"')


def is_middle_word(string):
    """Return if a word can be placed in the middle of the sentence."""

    return not string.istitle() and not string.endswith(".") and not string.endswith("!") and not string.endswith("?")


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
first_word = ""
while not is_first_word(first_word):
    first_word = random.choice(words)
first_word = first_word.split()
for i in range(10):
    sentence = sentence.join(first_word)
    count_word = 1

    while not is_final_word(first_word[0]) or count_word < 5:
        next_word = random.choices([key for key in ngrams[first_word[0]].keys()], [int(value) for value in ngrams[first_word[0]].values()])
        sentence = sentence + " " + next_word[0]
        count_word += 1
        first_word = next_word

    print(sentence)
    sentence = ""

    first_words = {key: value for key, value in ngrams[first_word[0]].items() if is_first_word(key)}
    try:
        first_word = random.choices([key for key in first_words.keys()], [int(value) for value in first_words.values()])
    except IndexError:
        first_word = random.choices([key for key in ngrams.keys() if is_first_word(key)])
