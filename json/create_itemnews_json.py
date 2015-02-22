#!/usr/bin/env python

import requests
import json
from lxml import html
from datetime import datetime

now_date = datetime.now()

with open('newsmodelism.json', 'r') as fp:
    items = json.load(fp)

url = raw_input("Enter a link: ")

r = requests.get(url)
tree = html.fromstring(r.text)

n = url[0:20]
print n

if n == "http://blog.oscarlia":
	print "Site: http://blog.oscarliang.net \n"
	print "Today is:", now_date.isoformat()
	pub = raw_input("Enter a date: ")
	# var_pub = "//meta[@property='article:published_time']/@content"
	var_tit = "//header[contains(@class, 'entry-header')]/h1/text()"
	var_paragrafs = "//div[contains(@class, 'e-content')]/p"
	var_images = "//div[contains(@class, 'e-content')]//img"
	site = "http://blog.oscarliang.net"
elif n == "http://helipilotonli":
	print "Site: http://helipilotonline.com \n"
	print "Today is:", now_date.isoformat()
	pub = raw_input("Enter a date: ")
	var_tit = "//*[@id='main-content']/div[contains(@class, 'content')]/article//h1/span/text()"
	var_paragrafs = "//*[@id='main-content']/div[contains(@class, 'content')]/article//div[contains(@class, 'entry')]/p"
	var_images = "//*[@id='main-content']/div[contains(@class, 'content')]/article//div[contains(@class, 'entry')]//img"
	site = "http://helipilotonline.com"
elif n == "http://www.rchelires":
	print "Site: http://www.rcheliresource.com/ \n"
	print "Today is:", now_date.isoformat()
	pub = raw_input("Enter a date: ")
	var_tit = "//*[@id='content']//div[contains(@class, 'post-title')]/h1/text()"
	var_paragrafs = "//*[@id='content']//div[contains(@class, 'post-content')]/p"
	var_images = "//*[@id='content']//div[contains(@class, 'post-content')]//img"
	site = "http://www.rcheliresource.com/"
else:
   print "Error"


# if n != "http://helipilotonli":
# 	pub = ''.join(tree.xpath(var_pub))
# else:
	# pub = var_pub

tit = tree.xpath(var_tit)
paragrafs = tree.xpath(var_paragrafs)
images = tree.xpath(var_images)

print "Categories: 'Aircraftflite', 'Helicopters', 'Multicopters', 'Parts', 'Video'"
cat = input("Enter a categories: ")

print cat

def lp(pp):
	for i in pp:
		p = i.xpath('text()|*/text()|*/*/text()|*/*/*/text()|*/*/*/*/text()')
		if len(p) > 0:
			return p

def li(ii):
	for x in ii:
		im = x.xpath('@src')
		return im

item = {
	'title': ''.join(tit),
	'img': ''.join(li(images)),
	'description': ''.join(lp(paragrafs)),
	'published': pub,
    'url': url,
    'categories': cat,
    'domain':'',
    'site': site 
}

print "\n -- Preview item -- \n\n", json.dumps(item, indent=2)

items[0:0] = [item]
with open('newsmodelism.json', 'w') as fp:
    json.dump(items, fp, indent = 4)
