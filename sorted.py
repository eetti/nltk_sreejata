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
dict_ = {}
 
read_file = "/Users/etti/Desktop/Sreejata/cnn_text.txt"

with open(read_file,"r") as r:
	# for line in r:
	filecontent = r.read()

tokenizer = RegexpTokenizer(r'\w+')
lowerCase = filecontent.lower()
allwords = lowerCase
words = tokenizer.tokenize(lowerCase) #tokenized_words


for w in words:
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

freqDist = nltk.FreqDist(stemmed) #words with high frequencies

tfidf = TfidfVectorizer(stop_words='english',max_features=15,analyzer='word',ngram_range=(1,15))
tfs = tfidf.fit_transform(filecontent.split('.'))

names = tfidf.get_feature_names()

word_msg = "No of words in document %d" %len(words)
print word_msg
print "_"*len(word_msg)

msg = "No of words after removing stopwords,digits and punctuations  : %d" % len(documents)
print msg
print "_"*len(msg)

stemmed_msg = "No of stemmed word %d" %len(stemmed)
print stemmed_msg
print "_"*len(stemmed_msg)

freq_msg = "Top 20 words with high frequencies"
print freq_msg
print "_"*len(freq_msg)

print freqDist.most_common(20)


tfidf_msg = "TF-IDF result for the document"
print tfidf_msg
print "_"*len(tfidf_msg)

for col in tfs.nonzero()[1]:
	# if names[col] not in dict_:
	# dict_[col] = tfs[0,col]
	print names[col],' - ',tfs[0,col]

