import csv
dir="./output.json"
if __name__=="__main__":
    with open(dir, encoding="utf-8") as f:
        i=0
        for x in f:
            i+=1
        print(i)