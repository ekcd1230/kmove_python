money=True
if money:
    print('현우햄 돼지')
else:
    print('수고추')

score=int(input('성적입력:'))
print('님의 성적은 %d 입니다.'%score)

if score >= 90:
    total='A'
elif score >= 80:
    total='B'
elif score >= 70:
    total='C'
elif score >= 60:
    total='D'
else:
    total='F'
print('니 성적은 {}다.'.format(total))