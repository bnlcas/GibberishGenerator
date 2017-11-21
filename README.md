# GibberishGenerator
This Repo contains python scripts to generate samples of gibberish text for research purposes.

The first script contains a set of functions to generate gibberish text samples from a bigram based markov model. 
The output will preserve the transition probabilities of the language given in the input corpus.

The second script contains a set of functions to generate gibberish text samples with a target sequence of characters embedded a specified number of times within the output.
The output gibberish will preserve the consonat-vowel transition probabilities and the distribution of characters from the sample corpus. It is also subject to additional contraints regarding the length and sequencing of words.

Both scripts require an input corpus given as a single string. A sample corpus text as well as sample outputs form the two scripts are provided.
