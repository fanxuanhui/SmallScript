#!/usr/bin/env python
#coding:utf-8
"""
 该模块的功能是对列表进行排序
	1、支持嵌套列表。
	2、支持数字字符混合型的列表
"""
def px(ll,level="z"):
"""
 这个函数接收2个参数：
	ll 是列表
	level 的值z代表，f代表反序排序
"""
    li = []
    for x in ll:
	if isinstance(x,list):
	    px(x)
	else:
	    li.append(x)
    for y in range(len(li)-1):
        for i in range(len(li)-1):
	    if li[i] > li[i+1]:
	        tmp = li[i]
	        li[i] = li[i+1]
	        li[i+1] = tmp
    if level == "z":
        return li
    elif level == "f":
	return li[::-1]	
	#return list(reversed(li))
	#return sorted(li,reverse=True)

#ll = [4,3,12,19,8,"b",3,1,"j","e",9,24,["a","1","b",5,2],4,"a","x"]
#p = px(ll,level="f")
#print(p)

	


