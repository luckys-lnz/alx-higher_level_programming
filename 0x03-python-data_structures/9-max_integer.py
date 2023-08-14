#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    bigest_num = my_list[0]
    for n in range(1, len(my_list)):
        if bigest_num < my_list[n]:
            bigest_num = my_list[n]
        else:
            continue
    return bigest_num
