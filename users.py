# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from matplotlib.backends.backend_pdf import PdfPages


log = False
inputname = "output.txt"
pdfname = "users.pdf"
pdfname2 = "users_shared.pdf"
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
    array.append([group,user,text, line2[3], line2[4],line2[5],line2[6]])
inputfile.close()

arr = np.array(array)
ugr = np.unique(arr[:,0])

udata = np.unique(arr[:,1]).tolist()

gr_data = []
nusers = []
num_user = 0
for i in range(len(ugr)):
    gr_data.append(np.unique(arr[arr[:,0] == ugr[i],1]).tolist())
for i in range(len(ugr)):
    for j in range(len(ugr)):
        if i>j:
            for k in gr_data[i]:
                if k in gr_data[j]:
                    nusers.append(int(k))
uniqusers = np.unique(nusers).tolist()
allusers = np.unique(arr[:,1]).tolist()

pp = PdfPages(pdfname2)
pl.clf()
fig = pl.figure(0)       
pl.hist(nusers,bins = np.arange(0,len(udata)+1),\
log=log, histtype=histtype, alpha=alpha, color = color)
pl.xlabel("users")
pl.ylabel("entries")
pl.grid()
pl.savefig(pp,format="pdf")
pp.close()

pp = PdfPages(pdfname)
pl.clf()
fig = pl.figure(1)
for i in range(len(ugr)):       
    name = ugr[i]
    ls_data = arr[arr[:,0] == name,1]
    nfroms = [int(i) for i in ls_data]
    pl.hist(nfroms,bins = np.arange(0,len(udata)+1),\
    log=log, histtype=histtype, alpha=alpha, label = name)
    pl.legend()
    pl.xlabel("users")
    pl.ylabel("entries")
    pl.grid()
    #pl.title("group %s" % (name,)) 
pl.savefig(pp,format="pdf")
pp.close()


