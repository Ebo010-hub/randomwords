#!/bin/python3

import random

def randomwords():
    with open("./MyFile.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
    
    for _ in range(len(words)):
        wordlist = random.choice(words)
        print(wordlist, end=" ") 

def count_words():
    with open("./MyFile.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
    return len(words)


def randomtext():
   while True:
    print("THIS IS THE TEXT")
    randomwords()
         
    choice = input ("\n¿Te gustó el resultado? ")
   
    if choice.lower() == "yes":
        break

if __name__ == '__main__':
    randomtext()
    print(f'El archivo tiene {count_words()} palabras.')
    randomtext()

   
