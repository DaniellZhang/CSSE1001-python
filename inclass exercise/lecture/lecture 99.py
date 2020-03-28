Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> apple
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    apple
NameError: name 'apple' is not defined
>>> 'apply'
'apply'
>>> 'apple'
'apple'
>>> 'red piece of fruit'
'red piece of fruit'
>>> d= 'apple':'red piece of fruit'
SyntaxError: invalid syntax
>>> d= ('\apple':'red piece of fruit')
SyntaxError: invalid syntax
>>> d= {'apple':'red piece of fruit'}
>>> 
>>> d
{'apple': 'red piece of fruit'}
>>> d= {1:'first no',(3,5):[2,7,8]}
>>> d
{1: 'first no', (3, 5): [2, 7, 8]}
>>> 
>>> d{'orange'}
SyntaxError: invalid syntax
>>> d['orange']
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d['orange']
KeyError: 'orange'
>>> d['orange']='orange piece of fruit'
>>> d['orange']
'orange piece of fruit'
>>> phone = {'Eric': 7724,'John': 9224,'Graham': 8462}
>>> phone
{'Eric': 7724, 'John': 9224, 'Graham': 8462}
>>> type(phone)
<class 'dict'>
>>> phone['John']
9224
>>> help(sorted)
Help on built-in function sorted in module builtins:

sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.

\
>>> phone['Terry']= 6352
>>> phone['Terry']
6352
>>> phone
{'Eric': 7724, 'John': 9224, 'Graham': 8462, 'Terry': 6352}
>>> phone = dict(Eric= 7724,John=9224, Graham=8462)
>>> phone
{'Eric': 7724, 'John': 9224, 'Graham': 8462}
>>> phone = dict(['Eric = 7724'])
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    phone = dict(['Eric = 7724'])
ValueError: dictionary update sequence element #0 has length 11; 2 is required
>>> 
========== RESTART: C:/Users/Daniel Zhang/Desktop/CSSSE/Lecture9.py ==========
>>> 
========== RESTART: C:/Users/Daniel Zhang/Desktop/CSSSE/Lecture9.py ==========
>>> load_anag(d,shortwords.txt)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    load_anag(d,shortwords.txt)
NameError: name 'd' is not defined
>>> d={}
>>> load_anag(d,shortwords.txt)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    load_anag(d,shortwords.txt)
NameError: name 'shortwords' is not defined
>>> load_anag(d,shortwords.txt)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    load_anag(d,shortwords.txt)
NameError: name 'shortwords' is not defined
>>> load_anag(d,shortwords.txt)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    load_anag(d,shortwords.txt)
NameError: name 'shortwords' is not defined
>>> load_anag(d,shortwords.txt)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    load_anag(d,shortwords.txt)
NameError: name 'shortwords' is not defined
>>> 
