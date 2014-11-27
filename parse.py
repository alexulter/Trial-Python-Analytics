# -*- coding: utf-8 -*-
from urllib import unquote
import re

mask = '[^A-Za-z0-9А-Яа-я]+'.decode('utf-8')
inputname = 'dz3.txt'
outputname = 'output.txt'
cutrepeat = True

inputfile = open(inputname, 'r')
outputfile = open(outputname,'w')
str_buff = ''
for line in inputfile:
    line = line.strip('\n')
    line = line.split(';')
    url = line[2]
    if cutrepeat:
        if url == str_buff :
            continue
        str_buff = url
    url2 = unicode(unquote(url),'utf-8', 'ignore')
#    url2 = url2.encode('cp866','ignore').decode('cp866','ignore')
#    url2 = url2.encode('cp1251','ignore').decode('cp1251','ignore')
#    print url2
    url3 = url2.split('&')
    url4 = ' '
    lr=' '
    msid = ' '
    family = ' '
    fullmode = ' '
    for piece in url3:
        if 'text=' in piece:
            url4 = piece
            url4 = url4[url4.find('text=')+5:]
            url4 = re.sub(mask, ' ', url4)
        elif 'lr=' in piece:
            lr = piece
            lr = lr[lr.find('lr=')+3:]
        elif 'msid=' in piece:
            msid = piece
            msid = msid[msid.find('msid=')+5:]
        elif 'family=' in piece:
            family = piece
            family = family[family.find('family=')+7:]
        elif 'fullmode=' in piece:
            fullmode = piece
            fullmode = fullmode[fullmode.find('fullmode=')+9:]
                
    user = ' '
    group = ' '
    if 'user=' in line[0]:
        user = line[0][5:]
    if 'group=' in line[1]:
        group = line[1][6:]
    outputfile.writelines(group+';'+user+';'+url4+';'+\
    lr+';'+msid+';'+family+';'+fullmode+'\n')

inputfile.close()
outputfile.close()
