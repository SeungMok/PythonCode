import re

# p = re.compile('ab*')

# m = p.match('bac')
# print(m)


# m1 = p.search('bac')
# print(m1)

email = input("email 입력 : ")
p = re.compile('[a-z][a-z0-9]{4,}@[a-z]{2,}.[a-z]{2,5}')
result = p.match(email)
print(result)