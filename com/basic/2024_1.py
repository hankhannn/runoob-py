#!/usr/bin/python

print("Hello World")
print('tornado, hurricane, volcano');
print('are natural disasters')

# python use indentation to indicate the code block
num = 5
if num >= 7:
    print('this is larger than ten')
    print('you got a good mark')
elif num > 3:
    print('middle range')
else:
    print('not bad')
    print('please try it again later')

line1 = 'one,'
line2 = 'two,'
line3 = 'three'
combineLines = line1 + \
               line2 + \
               line3
print(combineLines)

# be careful
word = "word"
sentence = 'This is a sentence'  # be careful too.
paragraph = """this is a paragraph, 
including multiple lines.
"""
print(word)
print(sentence)
print(paragraph)

'''
this is a multiple lines' explanation 
'''

a, b, c = 1, 2, 'John'
print(a, '\t', b, '\t', c)

hello = "hello world"
print(hello)
print(hello[0])
print(hello[-5])
print(hello[2:5])
print(hello[2:])
print(hello * 2)
print(hello + "TEST")

tuple = ('1111', 23, 2.23, 'just', 'ruooob')
tuple2 = ('1111', 23, 'just')
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tuple * 2)
print(tuple + tuple2)

dict = {'name': 'HANK', 'nationality': 'China'}
dict['gender'] = 'Male'
print(dict)
print(dict['name'])
print(dict.keys())
print(dict.values())


a = 21
b = 10
c = 0
c = a + b
print("c 的值为：", c)

a = 10
b = 5
c = a // b
print("c 的值为：", c)
