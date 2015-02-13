#!/usr/bin/env python

import requests
import json
from lxml import html

with open('newsmodelism.json', 'r') as fp:
    items = json.load(fp)

# url = 'http://blog.oscarliang.net/make-simple-whip-antenna-5-8ghz-linear-polo/'
url = raw_input("Enter a link: ")

r = requests.get(url)
tree = html.fromstring(r.text)

pub = tree.xpath("//meta[@property='article:published_time']/@content")
tit = tree.xpath('//header[contains(@class, "entry-header")]/h1/text()')
paragrafs = tree.xpath('//div[contains(@class, "e-content")]/p')
images = tree.xpath('//div[contains(@class, "e-content")]//img')

def lp(pp):
	for i in pp:
		p = i.xpath('text()|*/text()|*/*/text()|*/*/*/text()|*/*/*/*/text()')
		if len(p) > 0:
			# print p
			return p

def li(ii):
	for x in ii:
		im = x.xpath('@src')
		return im

item = {
	'title': ''.join(tit),
	'image': ''.join(li(images)),
	'description': ''.join(lp(paragrafs)),
	'published': ''.join(pub),
    'url':url,
    'categories':'Multicopters',
    'domain':''
}

print "\n -- Preview item -- \n\n", json.dumps(item, indent=2)

items[0:0] = [item]
with open('newsmodelism.json', 'w') as fp:
    json.dump(items, fp, indent = 4)
