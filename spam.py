import nltk
import random
from re import split
from nltk.corpus import stopwords

documents = []

#point to where you downloaded the file
read_file = "~/Desktop/Sreejata/SMSSpamCorpus01/english_big.txt"

with open(read_file,"r") as r:
   c =0
   for line in r:
   	#create the training document of labeled tuples
   	splitted = line.strip().split(',')
   	msg = (' ').join(splitted[:-1])
   	is_class = splitted[-1]
   	documents.extend([dict(doc=msg.lower(),category=is_class)])

#take out stopwords and any other garbage
all_words = nltk.FreqDist(w.lower() for d in documents for w in d['words'] if w not in stopwords.words() and not w.isdigit())

word_features = all_words.keys()[:2500]

#get features (words in this case)
def document_features(document):
	document['words'] = split('\W+',document['doc']) #split into words
	document_words = set(document['words']) #unique
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

random.shuffle(documents)

featuresets  =[(document_features(d),d['category']) for d in documents]

#split training and testing sets
train_set, test_set = featuresets[:1000],featuresets[1000:]

#classify using in-built Naive Bayes Classifier
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier,test_set)
classifier.show_most_informative_features(25)

print classifier.classify(document_features({'doc':"call for a free gift"}))