# wording-2022-python
### Dr E, 2022
project to find words in irrational numbers

Johannes wants to take some irrational numbr like pi=3.14159265258979...
and then search for words encoded according to some simple substitution 
code like 0=A, 1=B... 9=J. 

To jumpstart this, I figured I'd check the list of english words from
[https://github.com/dwyl/english-words] then use a regular expression to 
find all the ones that are 10 letters long and only have [a-j]. From there
one could then make an object for searching for the valid ones (which should
only be a few). 
