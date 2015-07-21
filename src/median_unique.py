# a program that will print the number of unique words per line
# sysmodule in python 2.7.4 is being used
import sys
#definition of fuctions to be used in calculation
medians = []
unique_words_per_tweet = []
#reading from the input text file containing all the tweets per line.
with open('tweets.txt', "r") as f:
        for line in f.readlines():
            unique_words = set(line.split())
            unique_words = len(unique_words)
            unique_words_per_tweet.append(unique_words)
            new_median = sum(unique_words_per_tweet) + unique_words/len(unique_words_per_tweet) + 1
            medians.append(new_median)
#write content of medians into your new text file ft2.txt
	    with open('ft2.txt','w+')as out:
        	print >> out, medians
