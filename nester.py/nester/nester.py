#!/usr/bin/env python
def print_lol(the_list, indent=False, level=0):
    for each_item in the_list:
	if isinstance(each_item,list):
	    print_lol(each_item , indent , level+1)
	else:
	    if indent:
	        for tab_srop in range(level):
		    print "\t",
	    print(each_item)

movies=["xx",123,"yy",1234,["zz",['aa',"bb"]]]
print_lol(movies,True,0)


