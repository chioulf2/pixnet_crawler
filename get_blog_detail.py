# -*- coding: utf8 -*-

import urllib2
import json

import time

#爬蟲 回傳dict 包含 圖片數 文字數 讚數
def get_blog_info(site, article_id, user):
	article_dict = {}
	url = 'https://emma.pixnet.cc/blog/articles/'+str(article_id)+'?user='+user+'&format=json'

	#先抓照片數
	response = urllib2.urlopen(url)
	response_json = response.read()
	# print(response_json)
	decode_json = json.loads(response_json)
	article_dict['photo_count'] = len(decode_json['article']['images'])
	# print(decode_json)
	# body = decode_json['body'].encode('UTF-8')
	# print(body)

	#再來用網址去爬 article-content裡面用正規表達拿文字數  然後拿FB讚數 然後用beautysoup

	time.sleep(0.5)
	return article_dict