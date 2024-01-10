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
