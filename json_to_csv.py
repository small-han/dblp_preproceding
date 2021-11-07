#-*-coding:utf-8-*-
import csv
import json
from re import I
import sys
import codecs

def trans(path):
    jsonData = codecs.open(path + '.json', 'r', 'ISO8859')
    # csvfile = open(path+'.csv', 'w')  # 此处这样写会导致写出来的文件会有空行
    # csvfile = open(path+'.csv', 'wb')  # python2下
    csvfile = open('dblp2.csv', 'w', newline='',encoding="utf-16")  # python3下
    writer = csv.writer(csvfile, delimiter=',')
    j=0
    for line in jsonData:
        j+=1
        if(j%1000==0):
            print(j)
        if(j==1000000):
            break
        dic = json.loads(line)
        # 获取属性列表
        authors= dic.get("author")
        if(authors!=None):
            authors_n=[]
            for i in authors:
                i_new=i
                authors_n.append(i_new)
            writer.writerow(authors_n)
    jsonData.close()
    csvfile.close()

if __name__ == '__main__':
    path="output"
    trans(path)