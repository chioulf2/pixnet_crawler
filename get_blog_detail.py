# -*- coding: utf8 -*-

import urllib2
import json

import time
import re

#爬蟲 回傳dict 包含 圖片數 文字數 讚數
def get_blog_info(site, article_id, user):
	article_dict = {} #存回傳結果

	#用來爬文章詳細api的
	api_url = 'https://emma.pixnet.cc/blog/articles/'+str(article_id)+'?user='+user+'&format=json'
	print(api_url)
	#先抓照片數
	response = urllib2.urlopen(api_url)
	response_json = response.read()
	decode_json = json.loads(response_json)

	article_dict['photo_count'] = len(decode_json['article']['images'])
	body = decode_json['article']['body'].encode('UTF-8')
	#regular expression
	p = re.compile('(<.*?>|&nbsp;|&darr;|<!--.*?-->)')	
	content = p.sub('',body)
	article_dict['content'] = content.replace(",","，")
	article_dict['content_count'] = len(content)
	# p = re.compile( '(one|two|three)') 
 	# print(p.sub( 'num', 'one word two words three words'))

	#再來用網址去爬 article-content裡面用正規表達拿文字數  然後拿FB讚數 然後用beautysoup
	from bs4 import BeautifulSoup

	response = urllib2.urlopen(site)
	response_html = response.read()
	#用beautyfulsoup解析html
	soup = BeautifulSoup(''.join(response_html))
	print(soup.html.head.title)
	

	time.sleep(0.5)
	return article_dict