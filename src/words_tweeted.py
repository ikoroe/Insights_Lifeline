from string import maketrans

word_list = open("tweets.txt", "r").read().split()
word_freq = {}

for word in word_list:
    if len(word): word_freq[word] = word_freq.get(word, 0) + 1

keys = sorted(word_freq.keys())
with open('ft1.txt','w')as out:
        for word in keys:
            print >> out, "%-20s %d" % (str(word), word_freq[word])
