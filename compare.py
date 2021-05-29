import numpy as np
from matplotlib import pyplot as plt
import csv
import pandas as pd
from nltk.tokenize import sent_tokenize
google_rating=0
positive_review=0
twitter_like=0
twitter_follower=0
twitter_tweet=0
facebook_like=0
facebook_follower=0
facebook_recommendation=0
hospital_list=[]
set1=[]
set2=[]
set3=[]
set4=[]
set5=[]
set6=[]
set7=[]
set8=[]
review_set=[]
facebook_set=[]
google_set=[]
twitter_set=[]
rating_set=[]
count=0
overall_rating=[]
with open('clinics.csv','r') as csvfile:
	reader =csv.reader(csvfile)
	for row in reader:
		if count == 0:
			count=count+1
		else:	
			hospital_list.append(row[1])		
			set1.append(row[5])
			if int(row[5]) > positive_review:
				positive_review = int(row[5])
			
			set2.append(row[6])
			if float(row[6])  > google_rating:
				google_rating = float(row[6])
			
			set3.append(row[7])
			if int(row[7])  > twitter_follower:
				twitter_follower = int(row[7])
			
			set4.append(row[8])
			if int(row[8])  > twitter_tweet:
				twitter_tweet = int(row[8])
			
			set5.append(row[9])
			if int(row[9])  > twitter_like:
				twitter_like = int(row[9])
			
			set6.append(row[10])
			if int(row[10])  > facebook_like:
				facebook_like = int(row[10])

			set7.append(row[11])
			if int(row[11])  > facebook_follower:
				facebook_follower= int(row[11])

			set8.append(row[12])
			if int(row[12])  > facebook_recommendation:
				facebook_recommendation = int(row[12])

#Content score #2*(Number of competitors+1)-(Rank in Published messages per account)-(Rank in Engagement per Post)+2
#Audience score #3*(Number of competitors+1)-(Rank in Avg. Followers per acccount)-(Rank in Total mentions)-(Rank in Branch reach)+3
#Care score #2*(Number of competitors+1)-(Rank in Response Rate)-(Rank in Avg response time)+2
for i in range(10):
	print("/////results of hospital- " + str(hospital_list[i]) +": ")
	review=float(set1[i])/positive_review
	review_set.append(review)
	print("score from reviews= "+str(review))
	google=float(set2[i])/google_rating
	google_set.append(google)
	print("score from google= "+str(google))
	twitter=1/3*(float(set3[i])/twitter_follower+float(set4[i])/twitter_tweet+float(set5[i])/twitter_like)
	twitter_set.append(twitter)
	print("score from twitter= "+str(twitter))
	facebook=1/3*(float(set6[i])/facebook_like+float(set7[i])/facebook_follower+float(set8[i])/facebook_recommendation)
	facebook_set.append(facebook)
	print("score from facebook= "+str(facebook))
	social_rating=20*google+20*facebook
	rating_set.append(1/40 *social_rating)
	
	form=40*review+20*google+20*twitter+20*facebook
	print("overall score = "+str(form))
	print("\n")
	overall_rating.append(form)
print("\n\n")
print("///////////////////////////////// Final Results //////////////////////////////")
for j in range(10):
	print(str(j+1)+")" + str(hospital_list[j]) +": "+ str(overall_rating[j]))	

n_groups = 10
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.15
opacity = 0.8
#ind=np.arange(N)
#width=0.35
rects1 = plt.bar(index, review_set, bar_width,alpha=opacity,color='r',label='Review Analysis')

rects2 = plt.bar(index + bar_width, twitter_set, bar_width,alpha=opacity,color='g',label='Twitter')
rects3 = plt.bar(index + 2*bar_width, facebook_set, bar_width,alpha=opacity,color='b',label='Facebook')
rects4 = plt.bar(index + 3*bar_width, google_set, bar_width,alpha=opacity,color='y',label='Google')
plt.xlabel('Hospitals')
plt.ylabel('Scores')
#plt.title('Scores by person')
plt.xticks(index+(bar_width)/2, ('Dr.Janet Castelino clinic','ASHU SKIN CARE','Oliva Clinic','Cosmoderma','Dr. Keshav Clinic','Clear Skin','Dr.Anita Rath clinic','DR.SURUCHI puri clinic','Dr venus clinic','PARISA Skin care'))
plt.yticks(np.arange(0, 1.05, 0.05))
plt.legend()

#plt.tight_layout()
plt.show()

n_groups = 10
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.4
opacity = 0.8
#ind=np.arange(N)
#width=0.35
rects = plt.bar(index, overall_rating, bar_width,alpha=opacity,color='b',label='overall_rating')
plt.xlabel('Hospitals')
plt.ylabel('Scores')
#plt.title('Scores by person')
plt.xticks(index+(bar_width)/2, ('Dr.Janet Castelino clinic','ASHU SKIN CARE','Oliva Clinic','Cosmoderma','Dr. Keshav Clinic','Clear Skin','Dr.Anita Rath clinic','DR.SURUCHI puri clinic','Dr venus clinic','PARISA Skin care'))
plt.yticks(np.arange(0, 105, 5))
plt.legend()

plt.tight_layout()
plt.show()


#form=4*(positive_review/high_review)+2*(google_rating/high_rating)+2*(likes/high_likes)+2*(followers/high_followers)
n_groups = 10
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.4
opacity = 0.8
#ind=np.arange(N)
#width=0.35
rects5 = plt.bar(index, review_set, bar_width,alpha=opacity,color='g',label='Rating based on Reviews')
rects6 = plt.bar(index + bar_width, rating_set, bar_width,alpha=opacity,color='b',label='Rating based on likes and followers')
plt.xlabel('Hospitals')
plt.ylabel('Scores')
#plt.title('Scores by person')
plt.xticks(index+(bar_width)/2, ('Dr.Janet Castelino clinic','ASHU SKIN CARE','Oliva Clinic','Cosmoderma','Dr. Keshav Clinic','Clear Skin','Dr.Anita Rath clinic','DR.SURUCHI puri clinic','Dr venus clinic','PARISA Skin care'))
plt.yticks(np.arange(0, 1.10, 0.05))
plt.legend()

plt.tight_layout()
plt.show()
