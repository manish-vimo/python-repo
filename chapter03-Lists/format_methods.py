# format() method
"""
The format() method formats the specified value(s) and insert them inside the string's placeholder.
The placeholder is defined using curly brackets: {}.
"""

txt="Hello {word}"
print(txt.format(word='World!'))

message1='Hi, My name is {} and I am {} years old.'
print(message1.format('Bob', 36))

message2='Hi, My name is {name} and I am {age} years old.'
print(message2.format(name='Bob', age=36))

message3 = 'Hi, My name is {0} and I am {1} years old.'
print(message3.format('Bob',36))