#!/usr/bin/env python
def print_lol(the_list):
    for each_item in the_list:
	if isinstance(each_item,list):
	    print_lol(each_item)
	else:
	    print(each_item)

#movies=["xx",123,"yy",1234,["zz",['aa',"bb"]]]
#print_lol(movies)


