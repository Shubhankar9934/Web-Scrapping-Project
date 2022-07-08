import csv
import json



f = open('Usa.json',encoding="utf8")
data = json.load(f)
# print(data)

fname = "output.csv"

with open(fname,"w") as file:
     csv_file = csv.writer(file)
     csv_file.writerow(["Course id","Course Name","Level","Degree",'Fee'])
     for item in data["result"]:
         temp=item.get("tuition_fee")
         temp2=temp.get("value")
         if(temp2==None): 
         
           continue
         csv_file.writerow([item.get['id'],item.get['title'],item.get['level'],item.get['degree'],item.get['tuition_fee']['value']])
       
   
       
