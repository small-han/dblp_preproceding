import csv
path_s="dblp1.csv"
path_d="dblp2.csv"
name_dic={}
name_f=50
def read_data():
    with open(path_s,encoding="utf-16")as f_s:
        reader=csv.reader(f_s)
        for line in reader:
            for name in line:
                count=name_dic.get(name)
                if(count==None):
                    name_dic[name]=0
                else:
                    name_dic[name]+=1

def fix_data():
    lest_name=0
    with open(path_s,encoding="utf-16")as f_s:
        with open(path_d,"w",encoding="utf-16",newline="")as f_d:
            reader=csv.reader(f_s)
            writer=csv.writer(f_d,delimiter=",")
            for line in reader:
                del_name=[]
                for name in line:
                    count=name_dic.get(name)
                    if(count<name_f):
                        del_name.append(name)
                for name in del_name:
                    line.remove(name)
                if (len(line)>1):
                    if(len(line)<10):
                        for i in range(9-len(line)):
                            line.append("?")

                    writer.writerow(line)

if __name__=="__main__":
    read_data()
    fix_data()






                    
