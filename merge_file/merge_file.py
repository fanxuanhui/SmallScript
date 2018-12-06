#!/usr/bin/env python
#coding:utf-8

with open('test01.txt') as f1:
	d1=f1.readlines()
	for line1 in d1:
		f1_port=line1.strip().split()[0]
		with open('test02.txt') as f2:
			d2=f2.readlines()
			flage=0            # 这里使用了一个flage
			for line2 in d2:
				f2_port=line2.strip().split()[0]
				if f1_port == f2_port:
					print(line1.strip()+"   "+line2.strip())	
			if flage==0:
				print(line1.strip())
