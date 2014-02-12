#!/usr/bin/env python

import sys
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    n = 2
    wordlist = corpus.split()
    worddict = {}  
    for i in range(len(wordlist)-2):
        x, y = "",""
        (x, y) = wordlist[i:i+n]
        keys = x,y

        if worddict.get(keys):
            worddict[keys].append(wordlist[i+2])
        else:
            worddict[keys] = [wordlist[i+2]]

    return worddict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    #TODO: Start with a capital letter
    #TODO: End with a punctuation (!?.)
    
    upper_bound = 100
    lower_bound = 2
    string = ""
    for i in range(lower_bound, upper_bound + 1):
        # Check to see if we are on the first loop by checking if i equals our
        # lower bound
        if i == lower_bound:
            # Instantiate the empty strings seed_x, since we need to test on it
            # before our script sets it.
            seed_x = ""

            # If seed_x (the first word in the string) isn't titlecase, keep
            # trying new random keys until it is.
            while not seed_x.istitle():
                # If seed_x isn't an titlecase, pick a new random key
                random_key = random.choice(chains.keys())
                # Save the values from the random key for concatting later
                seed_x, seed_y = random_key


        # If we aren't on the first loop
        else:
            # select a random word from the values assigned to chains[random_key]
            random_word = random.choice(chains[random_key])
            # set variables x and y to the values in the random_key tuple
            x, y = random_key
            # set random_key to be a new n-gram (2nd word of previous tuple, random word) 
            random_key = (y, random_word)
            # append the newest random_word to our string
            string = string + " " + random_word

    return seed_x + " " + seed_y + string 
    
    # return "Here's some random text."

def main():
    args = sys.argv
    f = open(args[1])


    # read input_text from a file
    input_text = f.read()
    f.close()
    f = open(args[2])
    input_text = input_text + f.read()
    f.close()

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()