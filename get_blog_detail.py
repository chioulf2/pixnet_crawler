# -*- coding: utf8 -*-

import urllib2
import json

import re
import time

#爬蟲 回傳dict 包含 圖片數 文字數 讚數
def get_blog_info(site, article_id, user):
	article_dict = {} #存回傳結果

	try:
		#用來爬文章詳細api的
		api_url = 'https://emma.pixnet.cc/blog/articles/'+str(article_id)+'?user='+user+'&format=json'
		print('loading '+api_url)
		#先抓照片數
		response = urllib2.urlopen(api_url)
		response_json = response.read()
		decode_json = json.loads(response_json)

		article_dict['photo_count'] = len(decode_json['article']['images'])
		#用正規表達去除tag 拿文字數 (跟html的article-content裡面一樣的東西)
		body = decode_json['article']['body'].encode('UTF-8')
		p = re.compile('(<.*?>|&nbsp;|&darr;|<!--.*?-->)')	
		content = p.sub('',body)
		article_dict['content'] = content.replace(",","，")
		article_dict['content_count'] = len(content)
		# p = re.compile( '(one|two|three)') 
	 	# print(p.sub( 'num', 'one word two words three words'))
 	except:
		print("error occur in situation2...")

	#再來用網址去爬 用beautyfulsoup拿FB讚數 
	from bs4 import BeautifulSoup

	try:
		#休息一下
		time.sleep(0.5)

		#fb plugin的網址 發現的規則
		article_dict['fb_likes'] = '' #先宣告出來 以利前面判斷

		fb_like_url = 'http://www.facebook.com/plugins/like.php?href='+site
		print('loading fb_like_url...')
		response = urllib2.urlopen(fb_like_url) 
		response_html = response.read()

		soup = BeautifulSoup(''.join(response_html))
		fb_like = soup.findAll("span", { "class" : "hidden_elem" })
		for like in fb_like:
			p = re.compile('[^0-9]') #將那段文字去除到只剩數字
			content = p.sub('',like.get_text())
			# print(content)
			article_dict['fb_likes'] = content
	except:
		# print("get fb like timeout")
		print("error occur in situation3...")


	# #用ghost.py
	# from ghost import Ghost
	# ghost = Ghost(wait_timeout = 30)
	# page,resources = ghost.open('https://www.facebook.com/plugins/like.php?href=http://jesse0218.pixnet.net/blog/post/30882673&layout=standard&show_faces=false&width=500&action=like&font=verdana&colorscheme=light&height=30')
	# # ghost.wait_for_page_loaded()
	# print(page.content)
	# article_dict['content_count'] = page.content
	# # ghost.show()
	# # ghost.sleep(2)

	return article_dict