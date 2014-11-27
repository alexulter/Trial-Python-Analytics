# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from matplotlib.backends.backend_pdf import PdfPages


log = True
inputname = "output.txt"
pdfname = "regions.pdf"
histtype = "step" #  "bar", "barstacked", "step", "stepfilled"
color = "green"
alpha = 0.5
comparison_mode = True
xmaxcut = 60    # 0 = turnoff
dataset = 3 # 3 = regions, 5 = family, 6 = fullmode

inputfile = open(inputname, "r")
array = []
for line in inputfile:
    line = line.strip("\n")    
    line2 = line.split(";")
    user = line2[1]
    group = line2[0]
    text = line2[2]
    array.append([group,user,text, line2[3], line2[4],line2[5],line2[6]])
inputfile.close()

arr = np.array(array)
ugr = np.unique(arr[:,0])
uls = np.unique(arr[:,3]).tolist()
umsid = np.unique(arr[:,4]).tolist()
ufam = np.unique(arr[:,5]).tolist()
ufull = np.unique(arr[:,6]).tolist()

if dataset == 3:
    data = uls
    xlabelname = 'region'
elif dataset == 4:
    data = umsid
    xlabelname = 'msid'
elif dataset == 5:
    data = ufam
    xlabelname = 'family'
elif dataset == 6:
    data = ufull
    xlabelname = 'fullmode'
else:
    data = uls
    xlabelname = 'region'

k = 0
for entry in arr[:,dataset]:
    if entry != ' ':
        k+=1
print(k)

### Здесь выводится гистограмма по регионам
pp = PdfPages(pdfname)
pl.clf()
if comparison_mode: fig = pl.figure(0)
for i in range(len(ugr)):
    if not comparison_mode:
        fig = pl.figure(i)        
    name = ugr[i]
    ls_data = arr[arr[:,0] == name,dataset]
    if dataset == 3:
        nfroms = []
        for i in ls_data:
            if i != ' ':
                nfroms.append(int(i))
    else:
        nfroms = [data.index(i) for i in ls_data]
    if not comparison_mode:
        pl.hist(nfroms,bins = np.arange(0,len(data)+1),\
        log=log, histtype=histtype, alpha=alpha, color=color)
    else:
        pl.hist(nfroms,bins = np.arange(0,len(data)+1),\
        log=log, histtype=histtype, alpha=alpha, label = name)
        pl.legend()
    pl.xlabel(xlabelname)
    pl.ylabel("entries")
    pl.grid()
    if not comparison_mode: 
        pl.title("group %s" % (name,)) 
        pl.savefig(pp,format="pdf")
if comparison_mode: 
    pl.savefig(pp,format="pdf")
pp.close()


