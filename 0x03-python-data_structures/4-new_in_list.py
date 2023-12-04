#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return newlist
    elif idx > len(my_list):
        return newlist
    else:
        newlist = my_list.copy()
        newlist[idx] = element
        return newlist
