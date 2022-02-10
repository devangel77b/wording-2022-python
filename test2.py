#/usr/bin/env python3

"""
test2.py
D Evangelista, 2022
Find all words in the English language that fit a pattern
Requires loading words.txt from https://github.com/dwyl/english-words
"""

import re # module with regular expressions


if __name__ == "__main__":

    re_object = re.compile(r"\b[a-j]{10}\b") # this line makes the search object

    for line in open("words.txt","r"):
        for match in re_object.finditer(line):
                print(match.group(0))

    
    
