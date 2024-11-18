# find

text = 'banana'
print(text.find('a'))  # 1
print(text.find('z'))  # -1

# index

print(text.index('a'))  # 1
# print(text.index('z'))  # ValueError

# isupper

string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper())  # True
print(string2.isupper())  # False


# islower

print(string1.islower()) # False
print(string1.islower()) # False

# isalpha

str = 'Hello'
str1 = '123lkjf3509sdf'

print(str.isalpha())  # True
print(str1.isalpha()) # False


# 문자열 조작 메서드(새 문자열 반환)

# replace

text = 'Hello, world! world world'
new_text = text.replace('world', 'Python')  
print(new_text)  # Hello, Python! Python Python

new_text1= text.replace('world', 'Python', 1)  
print(new_text1)  # Hello, Python! world world


# strip

text = ' *Hello, world!* '
new_text = text.strip()
print(new_text)

text='Hello, world!'
new_text1 = text.strip('H')
print(new_text1)

# split
text = 'Hello, World!, wer'
words = text.split(' ', 1)
print(words)  # ['Hello,', 'World!, wer']

words1 = text.split(',')
print(words1)  # ['Hello', 'World!', 'wer']

# join
words = ['Hello', 'world!']
next_words = '-'.join(words)
print(next_words)  # Hello-world!

# caplitalize

text = 'hELLo, WorlD!'
new_text = text.capitalize() # Hello, world!
print(new_text)

# title

text = 'heLLo, wOrlD!'
new = text.title() # Hello, World!
print(new) 

# upper
new_text1 = text.upper()  
print(new_text1)  # HELLO, WORLD!

# lower
new_text2 = text.lower()
print(new_text2)  # hello, world!

# swapcase

new_text3= text.swapcase()
print(new_text3) # HEllO,WoRLd!