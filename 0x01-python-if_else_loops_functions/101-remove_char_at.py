#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ''
    if n < 0:
        return (str)
    for i in str:
        if i == n:
            i += 1    
        new_str += chr(i)
    return (new_str)
