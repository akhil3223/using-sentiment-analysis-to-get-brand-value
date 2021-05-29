import nltk
#nltk.download('punkt') # one time execution
#nltk.download('stopwords') # one time execution
import numpy as np
import pandas as pd
import time
import datetime
import csv

from nltk.tokenize import sent_tokenize
import re
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
k=0
for k in range(10):
	infile1="review_"+str(k)+".csv"	
	##READ THE DATA
	print("STEP-1 Read file.....")
	start = datetime.datetime.now()
	df = pd.read_csv(infile1)
	end = datetime.datetime.now()
	delta = end-start
	print("............completed in time =".format(delta))


	##SPLIT TEXT INTO SENTENCES
	print("STEP-2 Split sentences.....")
	start = datetime.datetime.now()
	sentences = []
	cont=0
	for s in df['reviews']:
		if cont <= 1290:
			sentences.append(sent_tokenize(s))
			cont=cont+1
	sentences = [y for x in sentences for y in x] # flatten list
	end = datetime.datetime.now()
	delta = end-start
	print("............completed in time =".format(delta))


	##USE WORD EMBEDDINGS
	print("STEP-3 Extract word vectors.....")
	start = datetime.datetime.now()
	# Extract word vectors
	word_embeddings = {}
	f = open('glove.6B.100d.txt', encoding='utf-8')
	for line in f:
		values = line.split()
		word = values[0]
		coefs = np.asarray(values[1:], dtype='float32')
		word_embeddings[word] = coefs
	f.close()
	end = datetime.datetime.now()
	delta = end-start
	print("............completed in time =".format(delta))


	##TEXT PREPROCESSING
	print("STEP-4 TEXT PREPOCESSING.....")
	start = datetime.datetime.now()
	# 1)remove punctuations, numbers and special characters
	clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")

	# 2)make alphabets lowercase
	clean_sentences = [s.lower() for s in clean_sentences]

	stop_words = stopwords.words('english')

	# 3)function to remove stopwords
	def remove_stopwords(sen):
		sen_new = " ".join([i for i in sen if i not in stop_words])
		return sen_new

	# 4)remove stopwords from the sentences
	clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]
	end = datetime.datetime.now()
	delta = end-start
	print("............completed in time =".format(delta))


	##VECTOR REPRESENTATION OF SENTENCES
	print("STEP-5 WORD EMBEDDINGS AND VECTORS.....")
	start = datetime.datetime.now()
	# 1)Extract word vectors
	word_embeddings = {}
	f = open('glove.6B.100d.txt', encoding='utf-8')
	for line in f:
		values = line.split()
		word = values[0]
		coefs = np.asarray(values[1:], dtype='float32')
		word_embeddings[word] = coefs
	f.close()

	sentence_vectors = []
	for i in clean_sentences:
		if len(i) != 0:
			v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
		else:
			v = np.zeros((100,))
		sentence_vectors.append(v)
	end = datetime.datetime.now()
	delta = end-start
	print("............completed in time =".format(delta))


	##SIMILARITY MATRIX PREPARATION
	print("STEP-6 CREATING MATRIX .....(Note-takes more time)")
	start = datetime.datetime.now()
	# 1)similarity matrix
	print("len of matrix = "+str(len(sentences)))
	sim_mat = np.zeros([len(sentences), len(sentences)])

	# 2)initialize the matrix with cosine similarity scores
	for i in range(len(sentences)):
		for j in range(len(sentences)):
			if i != j:
				sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,100), sentence_vectors[j].reshape(1,100))[0,0]
	end = datetime.datetime.now()
	delta = end-start
	print("............completed in time =".format(delta))


	##APPLYING PAGE-RANK ALGORITHM
	print("STEP-7 APPLYING PAGE-RANK ALGORITHM.....")
	start = datetime.datetime.now()
	nx_graph = nx.from_numpy_array(sim_mat)
	scores = nx.pagerank(nx_graph)
	end = datetime.datetime.now()
	delta = end-start
	print("............completed in time =".format(delta))


	##SUMMARY EXTRACTION
	print("STEP-8 SUMMARY EXTRACTION.....")
	start = datetime.datetime.now()
	ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)

	# Extract top 150 sentences as the summary
	wid=150
	fname="ranked_sentences_"+str(k)+".csv"
	with open(fname, 'w', newline='') as file:
		writer = csv.writer(file)
		for i in range(wid):
			sentt=ranked_sentences[i][1]
			writer.writerow([sentt])

	end = datetime.datetime.now()
	delta = end-start
	print("............completed in time =".format(delta))













