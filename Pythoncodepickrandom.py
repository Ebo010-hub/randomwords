#!/bin/python3

# Python code to pick a random
# word from a text file
import random


def randonmwords():
    with open("./MyFile.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
    
    i = 1
    while i < len(words):
        words = list(map(str, allText.split()))
        wordlist = random.choice(words)
        print(wordlist, end=" ") 
        i += 1


if __name__ == '__main__':
   randonmwords()
