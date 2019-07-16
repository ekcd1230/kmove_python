import random
listLotto=[0,0,0,0,0,0]
ran = random.randint(1,45)
for i in range(0,5):
    for j in range(0,6):
        while ran in listLotto:
            ran=random.randint(1,45)
        listLotto[j]=ran
    listLotto.sort()
    print(listLotto)