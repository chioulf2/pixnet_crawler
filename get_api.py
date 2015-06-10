# -*- coding: utf8 -*-

import urllib2
import json

import csv
import time
import get_blog_detail as gbd

#作者清單
#'anise', 'bluehero', 'carriewang', 
user_list = ['jesse0218', 'meijuily',
			 'meiko1101', 'millychun', 'nellydyu', 'paine0602', 'sezna627']




for user in user_list:
	#存csv 一個人一個
	csv_title = str(user)+'.csv'
	f = open(csv_title,"w") 

	api_url = "https://emma.pixnet.cc/blog/articles?user="+user+"&format=json"
	print('loading '+api_url)
	response = urllib2.urlopen(api_url)
	response_json = response.read()
	decodejson = json.loads(response_json)

	#標頭
	f.write('標題' + ',')
	f.write('人氣' + ',')
	f.write('讚數' + ',')
	f.write('轉換率(讚數/人氣)' + ',')
	f.write('作者' + ',')
	f.write('作者個人分類(每個人不同)' + ',')
	f.write('照片數' + ',')
	f.write('內文' + ',')
	f.write('內文字數' + ',')
	f.write('Tag' + ',')
	f.write('\n')

	for i in decodejson['articles']:
		if(str(i['site_category_id']) == '26'):	#限定"美味食記"分類
			try:
				#獲得圖片數 字數 讚數
			    blog_info = gbd.get_blog_info(i['link'].encode('UTF-8'), i['id'], i['user']['name'])
			    if blog_info['fb_likes'] != '':
				    f.write(i['title'].encode('UTF-8') + ',')
				    f.write(str(i['hits']['total']) + ',')
				    f.write(str(blog_info['fb_likes']) + ',')
				    f.write(str(float(blog_info['fb_likes'])/float(i['hits']['total'])) + ',')
				    f.write(i['user']['name'] + ',')
				    f.write(i['category'].encode('UTF-8') + ',')
				    f.write(str(blog_info['photo_count']) + ',')
				    f.write(str(blog_info['content']) + ',')
				    f.write(str(blog_info['content_count']) + ',')
				    #讀取tag 並串接成一個欄位
				    final_tag = '' #串接所有tag用字串
				    for tag in i['tags']:
				    	final_tag += (tag['tag'].encode('UTF-8') + '/')
				    f.write(final_tag + ',')	

				    f.write('\n')
				    print("success!")
			except:
				print("error occur...")
			#休息一下
			time.sleep(0.5)

	print(user+" info done!")
	f.close()
	time.sleep(3)




# from ghost import Ghost
# ghost = Ghost(wait_timeout=30)
# page,resources = ghost.open('http://anise.pixnet.net/blog/post/42408028-%E6%9D%B1%E5%8D%80%E9%90%B5%E6%9D%BF%E5%9C%9F%E5%8F%B8%EF%BC%8E%E6%89%B6%E6%97%BA%E8%99%9F')
# ghost.wait_for_page_loaded(timeout=60)
# print(page.content)