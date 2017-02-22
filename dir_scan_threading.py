#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from Queue import Queue
import time
# import gevent
# from bs4 import BeautifulSoup as bs
# import re
import threading
from IPy import IP
import sys

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",}

class DirScan(threading.Thread):
	def __init__(self,queue):
		threading.Thread.__init__(self)
		self._queue = queue

	def run(self):
		while not self._queue.empty():
			url = self._queue.get_nowait()
			try:
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
	threads = []

	thread_count = 100
	for i in range(thread_count):
		threads.append(DirScan(queue))

	for t in threads:
		t.start()
	for t in threads:
		t.join()


if __name__ == '__main__':
	if len(sys.argv) == 2:
		start = time.time()
		main(sys.argv[1])
		print time.time()-start
		sys.exit(0)
	else:
		print 'Usage: %s 192.168.1.1/24'%(sys.argv[0])
		sys.exit(-1)