import time

input('''엔터를 누르고 20초를 셉니다.
20초 후에 다시 엔터를 누릅니다.(시작: Enter)''')
start=time.time()
input('')
finish=time.time()
result=int(finish-start)
print('실제시간: {}초 걸림'.format(result))
print('차이: {}초'.format(abs(20-result)))