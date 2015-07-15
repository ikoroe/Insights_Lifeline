# a program that will print the number of unique words per line
import sys
medians = []
unique_words_per_tweet = []
with open('tweets.txt', "r") as f:
        for line in f.readlines():
            unique_words = set(line.split())
            unique_words = len(unique_words)
            unique_words_per_tweet.append(unique_words)
            new_median = sum(unique_words_per_tweet) + unique_words/len(unique_words_per_tweet) + 1
            medians.append(new_median)
#write content of medians into your new f2.txt file here
with open('ft2.txt','a+')as out:
        print >> out, "%d" % medians
