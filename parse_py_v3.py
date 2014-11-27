import urllib.request
import re
#import numpy as np
#import pylab as pl
#from matplotlib.backends.backend_pdf import PdfPages


inputfile = open("dz3.txt", "r")
outputfile = open("output.txt","w")
#lines = []
array = []
group_list = []
for line in inputfile:
	line = line.strip('\n')
	line = line.split(';')
	#lines.append(line)
	url = line[2]
	url2 = urllib.request.unquote(url)
	#url2 = url2.encode('cp866','ignore').decode('cp866','ignore')
	#url2 = url2.encode('cp1251','ignore').decode('cp1251','ignore')
	url3 = url2.split("&")
	url4 = ""
	for text in url3:
		if 'text=' in text:
			url4 = text
			url4 = url4[url4.find('text=')+5:]
			url4 = re.sub('[^A-Za-z0-9А-Яа-я]+', ' ', url4)
	user = " "
	group = " "
	if 'user=' in line[0]: user = line[0][5:]
	if 'group=' in line[1]: group = line[1][6:]
	outputfile.writelines(group+";"+user+";"+url4+'\n')
	array.append([group, user, url4])
	#if group not in group_list:
	#	group_list.append(group)
	#else:
	#arr = np.array(mass)
	#ug = np.unique(arr[:,1])
	#for i in range(len(ug)):
		
	
	
inputfile.close()
outputfile.close()
