import random

array=random.sample(range(1,10),3)
print('답: {}'.format(array))

print('야구게임을 시작합니다.')
while True:
    strikecnt=0
    ballcnt=0
    num1=int(input('숫자 첫번째 입력: '))
    num2=int(input('숫자 두번째 입력: '))
    num3=int(input('숫자 세번째 입력: '))

    inputArray=[num1,num2,num3]
    print(inputArray)

    for i in range(3):
        while inputArray[i] in array:
            if array[i]==inputArray[i]:
                strikecnt+=1
            else:
                ballcnt+=1
            break
                
    print('{0}스트라이크 {1}볼'.format(strikecnt,ballcnt))
    if strikecnt==3:
        break
