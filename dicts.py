ks = {1 : 'a', 2:'b', 0:'aa'}
ks = sorted(ks, key = ks.get)
print(ks)