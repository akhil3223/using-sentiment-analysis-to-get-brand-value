#Step1 - Web scraping
Here we will scrap all the review data using chrome driver
chromedriver download link-"https://chromedriver.storage.googleapis.com/index.html?path=84.0.4147.30/"

commands to run-
	python3 facebook.py
	python3 google.py
	python3 practo.py



#Step2 - Text pre-processing
commands to run-
	python3 review.py




#Step3- Ranking text
Here we will rank all the review data  after pre-processing using "glove.6B.100d.txt"
glove.6B.100d.txt download link-"nlp.stanford.edu/data/glove.6B.zip"

commands to run-
	python3 text_rank.py



#Step4- Sentiment analysis
commands to run-
	python3 sentiment.py



#Step5- Data analysis
commands to run-
	python3 compare.py
