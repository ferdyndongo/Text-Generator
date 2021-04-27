# Text Generator
## Description
In this project, we will use a corpus that contains the entire script of **Game of
Thrones**. As the corpus will be used to "*train*" a probabilistic model that will
predict the next word in a chain of words, the generated text will resemble the style
and vocabulary of the source material. The naturalness of the generated text depends on the
data. The bigger the corpus, the better the results.  
To study how texts are structured, we usually have to take into consideration not just individual words but
sequences of words and the relationships between them. A sequence of any number of adjacent tokens is called
***n-gram***, where **n** is the number of tokens.  
After the training data is acquired and preprocessed, it has to be transformed into a *Markov chain model*.
The first step is to map the connections between tokens in the corpus. For this, we are going to use **bigrams**.  
The list of all bigrams can already be used to make some naive predictions but the data
contains a lot of repetitions: the total number of tokens is 10 times greater than the 
number of unique tokens. This ratio must be about the same in the list of bigrams. Some
bigrams might be very comon, others relatively rare.  
A ***Markov chain*** is a statistical model in which the probability of each event depends on the previous one.
It can be described as a set of states and transitions between them. Each transition has a probability that is 
determined by some kind of statistical data. In This project, a state corresponds to a token, and each transition
represents going from one word of a sentence to another. The probability of transitions is calculated from the
bigrams. The basic idea of this project is that from a dictionary we can create a model that will consider all
possible transitions from one word to another and choose the most probable one based on the previous word.  
Well, the model can already be used to predict the next word in a chain by feeding it any head (of a bigram) from
the corpus and retrieving the most probable tail from the corresponding entry. But how do we start the chain, what
should be the first word? A good way to start is to choose a random word from the corpus and feed it to the mode so
that it predicts the next word. After the next word is acquired, it should be used to predict the following word,
and so on, thus continuing the chain.
## Objectives
### Preprocess the text corpus in Text Generator
In order to prepare the corpus for use in this project, we need to take the following steps:
1. Open and read the corpus from the provided file *corpus.txt*. The filename should be
specified as user input.
2. Break the corpus into individual words. To create a *Markov model*, we use the simplest
form of *tokenization*: tokens are separated by whitespace characters such as spaces,
   tabulation, and newline characters. Punctuation marks should be left untouched since
   later on, they will play an important role in signaling where a sentence should need.
3. Acquire and print the following information about the corpus under the section of 
    the output called *Corpus statistics*:
   * the number of all tokens;
   * the number of all unique tokens, that is, the number of tokens without repetition.
4. Take an integer as user input and print the token with the corresponding index.
   Repeat this process until the string *exit* is input. Also make sur that the input index
   is actually an integer that falls in the range of the corpus. If that is not the case,
   print an error message and request a new input. Error messages should contain the 
   types of errors (*Type Error*, *Index Error*, *Value error*, etc).
### Break the dataset into bigrams and create Markov chain model
5. Transform the corpus into a collection of bigrams. The result should contain all the possible bigrams from
the corpus, which means that:
   - Every token from the corpus should be a head of a bigram with the exception of the last token which cannot
   become a head since nothing follows it;
   - Every token from the corpus should be a tail of a bigram with the exception of the first token which cannot
   possibly be the tail of a bigram because nothing precedes it.
6. Output the number of all bigrams in the corpus.
7. Take an integer as user input and print the bigrams with the corresponding index. repeat this process until the
     string *exit* is input.
8. The data should be reorganized in such a way that every head is repeated only once, and
all the possible tails can be directed accessed by querying that head and each tail should appear only once and
   the number of repetitions should be stored as in integer.
9. Besides creating the model, we should also check that it works correctly. To test it, let's take a string as 
user input and print all the possible tails and their corresponding counts. If the model does not contain the
   specified head, ask for another until it is valid. Repeat until the string *exit* is input.
### Generate random text
9. Choose a random word from the corpus that will serve as the first word of the chain
10. The second word should be predicted by looking up the first word of the chain in the model and choosing the 
most probable next word from the set of possible follow-ups until the length of the chain is 10 words, but this time
the current last word of the chain should be used to look up another probable word to continue the sentence.
11. To improve the quality of the generated sentences. We need to take into account the longer bits of the preceding
text. The list of bigrams should be transformed into a list of trigrams, but now, heads should consist of two-
    space-separated tokens concatenated into a single string. The tails still consist of one token.
