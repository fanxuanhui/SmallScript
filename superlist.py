#!/usr/bin/env python
#coding:utf-8
"""
这个模块的作用是判断输出列表的排序
这个模块可以接受2个参数：
	li传入的列表
	model 是判断是正序还是反序
"""
def superlist(li,model="z"):
	"""
		通过双层循环等到结果。
	"""
    for i in range(len(li)-1):
        for i in range(len(li)-1):
	    if model == "z":
                if li[i] > li[i+1]:
	            tmp = li[i]
	            li[i] = li[i+1]
	            li[i+1] = tmp
	    elif model == "f":
                if li[i] < li[i+1]:
	            tmp = li[i]
	            li[i] = li[i+1]
	            li[i+1] = tmp
    return li

#if __name__ == "__main__":    
#    li=[2,5,1,3,9,10,11,6,313,131,13113,12,24,14,11,15,9,5,3,2,4,3,2,1,10,3,2,5,5]
#    s = superlist(li,"f")
#    print(s)





