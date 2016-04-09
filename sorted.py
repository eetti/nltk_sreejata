import nltk
import random
from re import split
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk.tokenize import RegexpTokenizer

documents = []

# 
read_file = "/Users/etti/Desktop/Sreejata/cnn_text.txt"

with open(read_file,"r") as r:
	# for line in r:
	filecontent = r.read()
tokenizer = RegexpTokenizer(r'\w+')
lowerCase = filecontent.lower()
allwords = lowerCase
# documents.append(allwords)
filtered = tokenizer.tokenize(lowerCase)



# '''
for w in filtered:
	# remove stop words and digits
	if w not in stopwords.words() and not w.isdigit():
		documents.append(w)
		# stopWords += w
# '''
# print stopwords
print documents

# local_numbers = [x for x in range(0,100)]
# random.shuffle(local_numbers)

# print local_numbers

# print "amount" len(local_numbers) 
# print documents





# [[x for x in range(y,y-3)] for y in range(1,11)]

# stopwords = (for w in filecontent if w not in stopwords.words() and not w.isdigit())

# print filtered