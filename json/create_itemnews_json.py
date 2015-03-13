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
# print n

if n == "http://blog.oscarlia":
	print "Site: http://blog.oscarliang.net \n"
	var_tit = "//header[contains(@class, 'entry-header')]/h1/text()"
	var_paragrafs = "//div[contains(@class, 'e-content')]/p"
	var_images = "//div[contains(@class, 'e-content')]//img"
	site = "http://blog.oscarliang.net"
elif n == "http://helipilotonli":
	print "Site: http://helipilotonline.com \n"
	var_tit = "//*[@id='main-content']/div[contains(@class, 'content')]/article//h1/span/text()"
	var_paragrafs = "//*[@id='main-content']/div[contains(@class, 'content')]/article//div[contains(@class, 'entry')]/p"
	var_images = "//*[@id='main-content']/div[contains(@class, 'content')]/article//div[contains(@class, 'entry')]//img"
	site = "http://helipilotonline.com"
elif n == "http://www.rchelires":
	print "Site: http://www.rcheliresource.com/ \n"
	var_tit = "//*[@id='content']//div[contains(@class, 'post-title')]/h1/text()"
	var_paragrafs = "//*[@id='content']//div[contains(@class, 'post-content')]/p"
	var_images = "//*[@id='content']//div[contains(@class, 'post-content')]//img"
	site = "http://www.rcheliresource.com/"
elif n == "http://droneport.com":
	print "Site: http://droneport.com.ua \n"
	var_tit = "//*[@id='main-content']//div[contains(@class, 'content')]/article//h1/span/text()"
	var_paragrafs = "//*[@id='main-content']//div[contains(@class, 'content')]/article//div[contains(@class, 'entry')]/p"
	var_images = "//*[@id='main-content']//div[contains(@class, 'content')]/article//div[contains(@class, 'entry')]//img"
	site = "http://droneport.com.ua"
elif n == "http://www.heli-info":
	print "Site: http://www.heli-info.com \n"
	var_tit = "//div[contains(@class, 'post')]//*[contains(@class, 'post-title')]/text()"
	var_paragrafs = "//div[contains(@class, 'post')]//div[contains(@class, 'post-body')]//p"
	var_images = "//div[contains(@class, 'post')]//div[contains(@class, 'post-body')]//img"
	site = "http://www.heli-info.com"
else:
   print "Error"

tit = tree.xpath(var_tit)
paragrafs = tree.xpath(var_paragrafs)
images = tree.xpath(var_images)

print "Today is:", now_date.isoformat()
pub = raw_input("Enter a date: ")
if len(pub)>0:
	pub = pub
else:
	pub = now_date.isoformat()

print "Categories: 'Aircraftflite', 'Helicopters', 'Multicopters', 'Parts', 'Video', 'Transmitters', 'FPV'"
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

if images:
	image = ''.join(li(images))
else:
	image = raw_input("Enter a img: ")


if n == "http://www.heli-info":
	desc = ''
else:
	desc = ''.join(lp(paragrafs))


item = {
	'title': ''.join(tit),
	'img': image,
	'description': desc,
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
