import numpy as np
import pylab as pl
from matplotlib.backends.backend_pdf import PdfPages


log = True
inputname = "output.txt"
pdfname = "report.pdf"
histtype = "step" #  "bar", "barstacked", "step", "stepfilled"
color = "green"
alpha = 0.5
comparison_mode = True
xmaxcut = 60    # 0 = turnoff

inputfile = open(inputname, "r")
array = []
for line in inputfile:
    line = line.strip("\n")    
    line2 = line.split(";")
    user = line2[1]
    group = line2[0]
    text = line2[2]
    array.append([group,user,text])
inputfile.close()
pp = PdfPages(pdfname)
pl.clf()
arr = np.array(array)
ugr = np.unique(arr[:,0])

if comparison_mode: fig = pl.figure(0)
for i in range(len(ugr)):
    if not comparison_mode: fig = pl.figure(i)
    name = ugr[i]
    data = arr[arr[:,0] == name,2]
    spl_temp = [elem.split(" ") for elem in data]
    nwords = []
    for j in range(len(spl_temp)):
        temp_arr = np.array(spl_temp[j])
        value = np.where(temp_arr != "")[0].shape[0]
        nwords.append(value)
    if comparison_mode:
        pl.hist(nwords,bins = np.arange(0,np.max(nwords)+1),\
        log=log, histtype=histtype, alpha=alpha, label=name)
        pl.legend()
        x1,x2,y1,y2 = pl.axis()
        pl.axis((x1,20,y1,y2))
    else:
        pl.hist(nwords,bins = np.arange(0,np.max(nwords)+1),\
        log=log, histtype=histtype, alpha=alpha, color=color)
        pl.title("group %s" % (name,))    
    if xmaxcut > 0:        
        x1,x2,y1,y2 = pl.axis()
        pl.axis((x1,xmaxcut,y1,y2))
    pl.grid()
    pl.xlabel("words count")
    pl.ylabel("entries")
    if not comparison_mode: 
        pl.savefig(pp,format="pdf")
if comparison_mode: 
    pl.savefig(pp,format="pdf")
pp.close()