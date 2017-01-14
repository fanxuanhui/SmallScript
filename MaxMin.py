#!/usr/bin/env python
#coding:utf-8
print("############打印列表中的最大最小值###############")
li=[[10000,10,111,21313131],3,19,89,210,12,10,[4,3,4,2],5,100,99,62,26,191,102121,2122,[3,2,5]]
#max=li[0]
ll=[]
def PrintMax(the_li):
    for each in the_li:
	if isinstance(each,list):
	    PrintMax(each)
	else:
    	    ll.append(each)
    max=ll[0]
    min=ll[0]
    for i in range(len(ll)):
	if ll[i] > max:
	    max=ll[i]
	if ll[i] < min:
	    min=ll[i]
    return max,min
	

MAX,MIN=PrintMax(li)
print(MAX)
print(MIN)









