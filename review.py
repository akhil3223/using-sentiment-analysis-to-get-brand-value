import os
import csv
#cmd1='python3 google.py'
#cmd2='python3 facebook.py'
#cmd3='python3 practo.py'
#os.system(cmd1)
#os.system(cmd2)
#os.system(cmd3)

#p_count=0
for i in range(10):
	g_count=0
	f_count=0
	g_in="google_review_"+str(i)+".txt"
	f_in="facebook_review_"+str(i)+".txt"
	p_in="practo_review_"+str(i)+".txt"
	fi=open(g_in,"r")
	for line in fi:
		g_count=g_count+1
	fi.close
	fj=open(f_in,"r")
	for line in fj:
		f_count=f_count+1
	fj.close
	#fk=open(p_in,"r")
	#for line in fi:
	#	p_count=p_count+1
	#fk.close
	if g_count < 400:
		g_count=g_count-g_count/9
	elif g_count > 400 and g_count < 600:
		g_count=g_count-g_count/6
	elif g_count > 600 and g_count < 800:
		g_count=g_count-100
	elif g_count > 800:
		g_count=g_count-130
	#p_count=p_count-p_count/4	
	fi=open(g_in,"r")
	fj=open(f_in,"r")
	print(g_count)
	print(f_count)
	#fk=open(p_in,"r")
	fname="review_"+str(i)+".csv"
	with open(fname, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(["reviews"])
		for line in fi:
			if g_count > 0:
				writer.writerow([line])
				g_count=g_count-1
		for line in fj:
			if f_count == 1:
				if "null" not in line:
					writer.writerow([line])
			else:
				writer.writerow([line])
#		for line in fk:
#			if p_count > 0:
#				writer.writerow([line])
#	    			p_count=p_count-1
	fi.close()
	fj.close()
	#fk.close()













