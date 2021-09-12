from linecache import getline
f = open('input.txt', 'r')
a = f.read()
lines = a.split('\n')
for line in lines:
    words = line.split(' ')
    for word in words :
        if len(word) <= 5 : print(word)
