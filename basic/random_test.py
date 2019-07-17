import random

for i in range(0,5):
    listLotto=[0,0,0,0,0,0]
    for j in range(0,6):
        ran=0
        while ran in listLotto:
            ran=random.randint(1,45)
        listLotto[j]=ran
    listLotto.sort()
    print(listLotto)