# -*- coding: utf8 -*-

import urllib2
import json

#愛吃鬼云云食記
response = urllib2.urlopen("https://emma.pixnet.cc/blog/articles?per_page=20&user=anise&format=json")
response_json = response.read()
decodejson = json.loads(response_json)


import csv
import get_blog_detail as gbd



#存csv
f = open("article.csv","w") 
#標頭
f.write('標題' + ',')
f.write('人氣' + ',')
f.write('作者' + ',')
f.write('照片數' + ',')
f.write('內文' + ',')
f.write('內文字數' + ',')
f.write('Tag' + ',')
f.write('\n')


for i in decodejson['articles']:
	if(str(i['site_category_id']) == '26'):	#芸芸限定 美味食記
		# print('success')
	    f.write(i['title'].encode('UTF-8') + ',')
	    f.write(str(i['hits']['total']) + ',')
	    f.write(i['user']['name'] + ',')
	    #獲得圖片數 字數 讚數
	    blog_info = gbd.get_blog_info(i['link'].encode('UTF-8'), i['id'], i['user']['name'])
	    print(blog_info)
	    f.write(str(blog_info['photo_count']) + ',')
	    f.write(str(blog_info['content']) + ',')
	    f.write(str(blog_info['content_count']) + ',')
	    #讀取tag 並串接成一個欄位
	    final_tag = '' #串接所有tag用字串
	    for tag in i['tags']:
	    	final_tag += (tag['tag'].encode('UTF-8') + '/')
	    f.write(final_tag + ',')	

	    f.write('\n')

f.close()



