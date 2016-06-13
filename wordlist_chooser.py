#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
wordlist_chooser.py
-------------------

This is a program that chooses pseudo-random words
from the amazing mnemonic wordlist that can be found here:
http://web.archive.org/web/20090918202746/http://tothink.com/mnemonic/wordlist.html

The wordlist follows these rules:
1. The wordlist contains 1626 words with 6 columns.
2. All words are between 4 and 7 letters long.
3. No word in the list is a prefix of another word (e.g. visit, visitor).
4. Five letter prefixes of words are sufficient to be unique.


Usage: `python wordlist_chooser.py <number of words to pick>`

"""

from __future__ import print_function
from random import randrange
from sys import argv


def choose_one():
    rand_line = randrange(2, 274)
    rand_word = randrange(0, 5)
    with open('wordlist.txt') as f:
        f.next()  # skip first line
        for i, line in enumerate(f):
            if i == rand_line:
                return line.split()[rand_word]


def choose_words(amt=1):
    for i in range(amt):
        print(choose_one())


def main():
    try:
        int(argv[1])
    except IndexError:
        amt = 1
    else:
        amt = int(argv[1])
    finally:
        choose_words(amt)


if __name__ == "__main__":
    main()
