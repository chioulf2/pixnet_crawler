# -*- coding: utf8 -*-

import urllib2
import json

#愛吃鬼云云食記
response = urllib2.urlopen("https://emma.pixnet.cc/blog/articles?per_page=10&user=anise&format=json")
response_json = response.read()

decodejson = json.loads(response_json)

# print decodejson['articles']

import csv
data = []

# print decodejson

for i in decodejson['articles']:
	row_data = []
	row_data.append(i['title'].encode('utf-8'))
	row_data.append(i['hits']['total'])
	data.append(row_data)

#print data

#存csv
f = open("article.csv","w") 
w = csv.writer(f)
w.writerows(data)
f.close()