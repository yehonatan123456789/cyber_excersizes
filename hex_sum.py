import re
word = input("please enter a word: ")
List = re.findall("[0-9a-f]", word)
# print(List)

sum = 0
for i in List:
    sum = sum + int(i, base=16)
print(sum)