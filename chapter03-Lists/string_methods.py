text = 'Jean-Paul Sartre somewhere observed that we each of us make our own hell out of the people around us. Had Jean-Paul known Nancy, he may have noted that at least one man, someda y, might get very lucky, and make his own heaven out of one of the people around him. She will be his morning and his evening star, shining with the brightest and the softest light in his heaven. She will be the end of his wanderings, and their love will arouse the daffodils in the spring to follow the crocuses and precede the irises. Their faith in one another will be deeper than time and their eternal spirit will be seamless once again.'

# find the first index of the substring 'Nancy' 
print(text.find('Nancy'))

# replace the substring 'Nancy' with 'Nancy Lier Cosgrove Mullis'
print(text.replace('Nancy', 'Nancy Lier Cosgrove Mullis'))

print()

# convet the text to lower case
print(text.lower())

print("====")

#convert the first letter of the text to capital letter
print(text.capitalize())

print()
# casefold() method returns a string where all the characters are in lower case
print(text.casefold())

print("=======")


# count() method returns the number of elements with the specified value
print(text.count('and'))


