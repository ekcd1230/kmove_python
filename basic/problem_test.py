import random
import time

cnt=0
start=time.time()
for i in range(5):
    a=['+','-','*','/']
    ran1=random.randint(1,10)
    ran2=random.randint(1,10)
    ran3=random.randint(0,3)
    problem='{0} {1} {2}'.format(ran1,a[ran3],ran2)
    print(problem)
    inputValue=int(input('정답입력:'))
    
    
    result=int(eval(problem))
    if inputValue==result:
        print('정답')
        cnt+=1
    else:
        print('오답, 정답은 {}'.format(result))
finish=time.time()
a=int(finish-start)
print('{0}개 맞춤, {1}초 걸림'.format(cnt,a))