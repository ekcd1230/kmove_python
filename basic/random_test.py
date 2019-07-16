import random
listLotto=[0,0,0,0,0,0]

for i in range(0,6):
    listLotto.pop(i)
    listLotto.insert(i,random.randint(1,45))

print(listLotto)