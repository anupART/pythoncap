
# LIST METHOD
li=["anup","captain",67,9792,'python']


li.append(45)
print(li)

li.clear()
print(li)

print(li.copy())


# li2=["extend1",'extend2',456]
# li.extend(li2)
# print(li)

# print(li.index("anup"))

# print(li.pop(2))

# a=li.remove('python')
# print(a)

# li.reverse()
# print(li)

# li.sort
# print(li)



# STRINGS

s="i am Anup and I am learning PYTHON with my captain"

print(s.capitalize())
print(s.casefold())
print(s.center(89))
print(s.encode())
print(s.endswith("N"))
print(s.find("Anup"))
print(s.index("am"))
print(s.format("i"))
# print(s.isalpha())
# print(s.isascii())
# print(s.isdigit())
# print(s.isdecimal())
# print(s.isnumeric())
# print(s.istitle())
# print(s.isascii())
# print(s.isidentifier())
# print(s.isspace())



# The negative index is used to remove any new-line spaces from the string and allow the string to except the last character that is given as S[:-1]

negative="python program"
print(negative[-2])
print(negative[-3:-1])
print(negative[::-4])

