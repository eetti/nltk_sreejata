import nltk
import random
from re import split
from nltk.corpus import stopwords
from nltk.stem.porter import *
from nltk import FreqDist
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter

documents = []
dict_ ={}
 
read_file = "~/Sreejata/cnn_text.txt"

with open(read_file,"r") as r:
	# for line in r:
	filecontent = r.read()
tokenizer = RegexpTokenizer(r'\w+')
lowerCase = filecontent.lower()
allwords = lowerCase
filtered = tokenizer.tokenize(lowerCase)


for w in filtered:
	# remove stop words and digits
	if w not in stopwords.words('english') and not w.isdigit():
		documents.append(w)

		
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

stemmer = PorterStemmer()
stemmed = stem_tokens(documents, stemmer)

tfidf = TfidfVectorizer(stop_words='english',max_features=10)
tfs = tfidf.fit_transform(stemmed)

names = tfidf.get_feature_names()

msg = "Number of words in the bag of words  : %d" % len(documents)

print msg
print "_"*len(msg)
print "Meaning full terms"
print "_"*len(msg)

for col in tfs.nonzero()[1]:
	if names[col] not in dict_:
		dict_[tfs[col]] = tfs[0,col]
		print names[col],' - ',tfs[0,col]

