# encoding=utf8
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
import time
import argparse
import os
import re
import csv
import pandas as pd
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

#options = Options()
#options.add_argument('--headless')
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage')
##options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application"

infile = 'clinic_list.csv'
i=0
cnt=0

with open(infile, 'r') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		if cnt > 0:
			#print(row[3])
			url=row[3]
			print(url)
			driver = webdriver.Chrome('webdrivers/chromedriver')
			#driver.get('https://www.google.com/search?rlz=1C1CHBF_enIN873IN873&sxsrf=ACYBGNRAo1AIntP0gf_Zbpkfbt1ijISGTg:1575922899958&q=e+fitness+studio+new+gym&npsic=0&rflfq=1&rlha=0&rllag=17465899,78359604,907&tbm=lcl&ved=2ahUKEwjDyJSlsqnmAhUHwTgGHXmpBgIQjGp6BAgMEEU&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u16!2m2!16m1!1e1!1m4!1u16!2m2!16m1!1e2!2m1!1e2!2m1!1e3!2m1!1e16!3sIAE,lf:1,lf_ui:2&rldoc=1#lrd=0x3bcb936c52ce8bfd:0xddd3f0887e725c8b,1,,,&rlfi=hd:;si:15984383971495664779,l,ChhlIGZpdG5lc3Mgc3R1ZGlvIG5ldyBneW1aIwoHbmV3IGd5bSIYZSBmaXRuZXNzIHN0dWRpbyBuZXcgZ3lt;mv:[[17.5040077,78.4194413],[17.3963259,78.32607829999999]]')
			#driver.get('https://www.google.com/search?q=dr+venus+hospital&rlz=1C1CHBF_enIN873IN873&oq=dr&aqs=chrome.0.69i59j69i57j69i59j0j69i60l4.1257j0j7&sourceid=chrome&ie=UTF-8#lrd=0x3bcb92895dc3cf6b:0x296c1886e753d824,1,,,')
			driver.get(url)
			time.sleep(15)
			print("Chrome Browser Invoked")
			pause_time = 5
			# Get scroll height
			last_height = driver.execute_script("return document.getElementById('reviewSort').scrollHeight;")

			# Record the starting time
			start = datetime.datetime.now()

			while True:
				# Scroll down to bottom
				driver.execute_script("document.getElementsByClassName('review-dialog-list')[0].scrollTo(0,document.getElementById('reviewSort').scrollHeight);")

				# wait to load page
				time.sleep(pause_time)

				# Calculate new scroll height and compare with last scroll height
				new_height = driver.execute_script("return document.getElementById('reviewSort').scrollHeight;")
				if new_height == last_height: # which means end of page
					break
				# update the last height
				last_height = new_height

			# Record the end time, then calculate and print the total time
			end = datetime.datetime.now()
			delta = end-start
			print("[INFO] Total time taken to scroll till the end {}".format(delta))

			#userid_element = driver.find_elements_by_xpath('//*[@id="reviewSort"]/div/div[2]/div[1]/span[1]/a[2]')[0]
			#userid = userid_element.text
			user_message = driver.find_elements_by_xpath('//*[@id="reviewSort"]')[0]
			#data = browser.find_element_by_class_name('r-i0Yz6hTjO7Ag')
			#search = driver.find_elements_by_id('reviewSort')[0]
			#for item in user_message: 
			#    text = item.text 
			#    print(text)
			comment = user_message.text
			fi = open("google.txt","w")
			fi.write(comment)
			fi.close()
			fj = open("google.txt","r")
			count=0
			prev=0
			inf="google_review_"+str(i)+".txt"
			fk= open(inf,"w")
			for line in fj:
				#print(re.search("^[0-9].review|reviews$",line))
				if re.search("^[0-9].review|reviews$",line) or re.search("^Local Guide(.*)photo|photos$",line):
				
					prev=prev+1
				
				#print(line)
				#print(prev)
				if prev == 3 :
					if re.search("^Response(.*)ago$",line):
						print(" ")
					else:
						count=count+1
						print(count)
						print(line)
						fk.write(line)
						#print(prev)
						prev = 0
				elif prev > 0 & prev < 3:
					#print(prev)
					prev=prev + 1
			fk.close()
			fj.close()
			i=i+1
		else:
			cnt=cnt+1
