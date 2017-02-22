#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from Queue import Queue
import time
import gevent
from gevent import monkey; monkey.patch_all()
# from bs4 import BeautifulSoup as bs
# import re
from IPy import IP
import sys

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",}

def spider(queue):
	while not queue.empty():
		url = queue.get_nowait()
		try:
			# print url
			r = requests.get(url=url, timeout=6, headers=HEADERS)
			print r.status_code,url
			
		except Exception,e:
			# print e
			pass


def create(ips):
	queue = Queue()
	ip = IP(ips, make_net=True)

	for i in ip:
		queue.put('http://'+str(i))
	return queue

def main(ips):
	queue = create(ips)
	gevent_pool = []

	thread_count = 100
	for i in range(thread_count):
		gevent_pool.append(gevent.spawn(spider,queue))
	gevent.joinall(gevent_pool)


if __name__ == '__main__':

	if len(sys.argv) == 2:
		start = time.time()
		main(sys.argv[1])		
		print time.time()-start
		sys.exit(0)
	else:
		print 'Usage: %s 192.168.1.1/24'%(sys.argv[0])
		sys.exit(-1)