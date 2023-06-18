from random import randint
s=[randint(1, 10) for x in range(10)]
s1=[i for i in s if 3 < i < 8]
print(s)
print(s1)
print(sum(s1))