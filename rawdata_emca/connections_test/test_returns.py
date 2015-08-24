"""
Created on Feb 16, 2015

@author: Jason Bowles
"""
import pandas as pd
import numpy as np
import csv

if __name__ == '__main__':
    dates = pd.date_range('20130101',periods=6)
    df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
    print df.to_csv(index_label="Index")
    dictList = []
    randHdr = ['Index','A','B','C','D']
    randIndex = ['2013-01-01','2013-01-02','2013-01-03','2013-01-04','2013-01-05','2013-01-05']
    randList = np.random.randn(6,4)
    randGroup = []
    #print randList
    randGroup.append(randHdr)
    for i in xrange(len(randList)):
        itemList = []
        adict = {}
        itemList.append(randIndex[i])
        j = 0
        adict[randHdr[j]] = randIndex[i]
        for item in randList[i]:
            j = j + 1
            adict[randHdr[j]] = item
            itemList.append(item)
        randGroup.append(itemList)
        dictList.append(adict)
    
    action = 'a'
    with open('some.csv', action) as f:
        writer = csv.writer(f,lineterminator='\n')
        tempfile = open('new_some.csv','r')
        reader = csv.reader(tempfile)
        reader.next()
        for row in reader:
            writer.writerow(row)
        
        #writer = csv.DictWriter(f,lineterminator='\n', fieldnames=randHdr)
        #if action != 'a':
        #    writer.writeheader()
        #writer.writerows(dictList)
        
    