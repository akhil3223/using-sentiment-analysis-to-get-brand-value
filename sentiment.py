import csv
import numpy as np
from textblob import TextBlob
from matplotlib import pyplot as plt
N_positive=[]
N_negative=[]
#N_neutral=[]
#prev=" "
for i in range(10):
	infile = "ranked_sentences_"+str(i)+".csv"
	#infile="review_"+str(i)+".csv"
	positivity=0
	#neutrality=0
	negativity=0
	with open(infile, 'r') as csvfile:
		rows = csv.reader(csvfile)
		for row in rows:
			sent = row[0]
			#if sent != prev:
			#prev=sent
			blob = TextBlob(sent)
			polar = blob.sentiment.polarity
			if(polar > 0):
				#print("positive review ="+sent+"with polarity ="+str(polar))
				positivity=positivity+1
				
			if(polar <= 0):
				#print("negative review ="+sent+"with polarity ="+str(polar))
				negativity=negativity+1
		#	if(polar > -0.1 and polar < 0.1):
		#		print("neutral review")
		#		neutrality=neutrality+1

	print("number of positive comments: " + str(positivity)+" and negative comments: " + str(negativity))
	N_positive.append(positivity)
	N_negative.append(negativity)
#	N_neutral.append(postivity)

N=10
n_groups = 10
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
#ind=np.arange(N)
#width=0.35
rects1 = plt.bar(index, N_positive, bar_width,alpha=opacity,color='b',label='Positive review')

rects2 = plt.bar(index + bar_width, N_negative, bar_width,alpha=opacity,color='g',label='Negative review')
plt.xlabel('Hospitals')
plt.ylabel('Scores')
#plt.title('Scores by person')
plt.xticks(index+(bar_width)/2, ('Dr.Janet Castelino clinic','ASHU SKIN CARE','Oliva Clinic','Cosmoderma','Dr. Keshav Clinic','Clear Skin','Dr.Anita Rath clinic','DR.SURUCHI puri clinic','Dr venus clinic','PARISA Skin care'))
plt.yticks(np.arange(0, 176, 10))
plt.legend()

plt.tight_layout()
plt.show()

#p1 = plt.bar(ind, postivity, width)
#p2 = plt.bar(ind, negativity, width,bottom=postivity)
#p3 = plt.bar(ind, neutrality, width,
#             bottom=negativity)
#colors = ['#E69F00', '#56B4E9', '#F0E442']
#names = ['Postive reviews', 'Negative reviews', 'Neutral reviews'] 
#plt.ylabel('Scores')
#plt.xticks(ind, ('Dr.Venus','','g3','g4','g5','g6','g7','g8','g9','g10'))
#
#plt.legend((p1[0], p2[0],p3[0]), ('Postive reviews', 'Negative reviews', 'Neutral reviews'))
#plt.legend((p1[0], p2[0]), ('Postive reviews', 'Negative reviews'))
#plt.figure()
#plt.hist([postivity,negativity,neutrality], bins, stacked=True, density=True color=colors,label=names)
#plt.show()


