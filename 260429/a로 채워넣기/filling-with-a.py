

str = input()
leng = len(str)
str = str[0] + 'a' + str[2:]
str = str[:leng-2] + 'a' + str[-1]

print(str)