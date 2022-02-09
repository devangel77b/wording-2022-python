"""
test1.py
D Evangelista, 2022
Test code for just getting regular expressions to find all the words 
in a piece of text that consist only of letters a-j and are of length 3.
"""

import re # module with regular expressions

# my test text is defined on the next line... 
TEXT = """abc bcd cde def efg fgh ghi hij ijk jkl jlm abcd bcde cdef"""

if __name__ == "__main__":

    re_object = re.compile(r"\b[a-j]{3}\b") # this line makes the search object
    result = re_object.findall(TEXT) # this line runs the search
    print(result) # the result is a list of the positives

    
    
