#a program that calculates the total number of times each word has been tweeted.
#maketrans module in python is used.
from string import maketrans
#definition of the count parameters for input text file in 'tweets'
word_list = open("tweets.txt", "r").read().split()
word_freq = {}

for word in word_list:
    if len(word): word_freq[word] = word_freq.get(word, 0) + 1
#definition of the key fuction and the print out statement that will take out to a new text file ft1
keys = sorted(word_freq.keys())
with open('ft1.txt','w')as out:
        for word in keys:
            print >> out, "%-20s %d" % (str(word), word_freq[word])
