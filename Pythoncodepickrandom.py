# Python code to pick a random
# word from a text file
import random

i = 1
while i < 500:
      with open("./MyFile.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        wordlist = random.choice(words)
        wordlist1 = random.choice(words)
        wordlist2 = random.choice(words)
        wordlist3 = random.choice(words)
        wordlist4 = random.choice(words)
        wordlist5 = random.choice(words)
        wordlist6 = random.choice(words)
       print (wordlist+' '+wordlist1+' '+wordlist2+' '+wordlist3+'                              '+wordlist4+' '+wordlist5+' '+wordlist6)
       i += 1
