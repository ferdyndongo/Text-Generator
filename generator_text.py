#!/usr/bin/env python3

from nltk.util import ngrams
from nltk import Text
from collections import Counter
import random
import re


def markov_chain(string, n):
    """Return a dictionary with Markov chain model where the next word depends on the n preceding words given a sequence of words and n in input)."""

    if n in range(2):
        print("The Markov model needs n to be >= 2 to be built.")
        n_grams = list(ngrams(string, n))
        return n_grams
    else:
        grams = list(ngrams(string, n))
        n_grams = {}
        for gram in grams:
            head = gram[0]
            for r in range(1, (len(gram) - 1)):
                head += " " + gram[r]
            tail = gram[-1]
            if head not in n_grams:
                n_grams[head] = {tail: 1}
            else:
                if tail in n_grams[head]:
                    n_grams[head][tail] += 1
                else:
                    n_grams[head][tail] = 1
        return n_grams


def is_first_word(string):
    """Return if a word can be placed in the beginning of the sentence."""

    if re.match(r"[A-Z].+[^\W]$", string):
        return True
    else:
        return False


def is_final_word(string):
    """Return if a word is placed at the end of the sentence."""

    if re.match(r".+[.!?]$", string):
        return True
    else:
        return False


# Preprocess the text
text = input()
words = []
with open(text, 'r', encoding='utf-8') as corpus:
    for row in corpus:
        for word in row.split():
            words.append(word)
corpus = Text(words)
print(f"""Corpus statistics
All tokens: {len(corpus)}
Unique tokens: {len(Counter(corpus))}
""")

# Create a Markov chain model
bi_grams = markov_chain(corpus, 2)
tri_grams = markov_chain(corpus, 3)

# The first word is chosen random word
first_word = random.choices([key for key in bi_grams.keys() if is_first_word(key)])

# Generate 10 random sentences
for i in range(10):
    sentence = ""
    sentence = sentence.join(first_word)
    # The second word is chosen with respect to the most probable in the bi-gram markov chain model given the first one
    next_word = random.choices([key for key in bi_grams[first_word[0]].keys()], [int(value) for value in bi_grams[first_word[0]].values()])
    sentence += " " + next_word[0]
    first_word = [sentence.split()[-2] + " " + sentence.split()[-1]]
    while not is_final_word(next_word[0]):
        # The following words are chosen given the preceding two with respect to the most probable in the tri-gram markov chain model
        next_word = random.choices([key for key in tri_grams[first_word[0]].keys()], [int(value) for value in tri_grams[first_word[0]].values()])
        sentence = sentence + " " + next_word[0]
        first_word = [sentence.split()[-2] + " " + sentence.split()[-1]]

    print(sentence)
    first_word = random.choices([key for key in tri_grams[first_word[0]].keys()], [int(value) for value in tri_grams[first_word[0]].values()])
