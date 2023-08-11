#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ""
    i = 0
    for c in str:
        if i != n:
            new_string += c
        i += 1
    return new_string
