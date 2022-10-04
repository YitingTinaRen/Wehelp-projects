import urllib.request as req
import json
import csv
url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with req.urlopen(url) as reponse:
    data = json.load(reponse)

data=data["result"]["results"]
# print(len(data))
# print(int(data[0]["xpostDate"][0:4]))
with open('data.csv', 'w') as csvfile:
    writer=csv.writer(csvfile)
    for i in range(len(data)):
        if int(data[i]["xpostDate"][0:4])>=2015:
            # Get the first image url
            imgurl=data[i]["file"]
            imgurl=imgurl.split('https://')
            imgurl="https://"+imgurl[1]
            writer.writerow([data[i]["stitle"], data[i]["address"][5:8], data[i]["longitude"], data[i]['latitude'], imgurl])
