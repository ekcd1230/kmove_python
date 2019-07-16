listdata=[1,2,3]
while True:
    print('''
    ======================= 리스트 데이터 관리 =======================
    1. 리스트에 추가      2. 리스트 데이터 수정   3. 리스트 데이터 삭제 4. 종료
    ''')
    menu = int(input('메뉴를 선택: '))

    if menu == 4:
        print('=======종료=======')
        break
    elif menu == 1:
        data=input('추가할 데이터를 입력:')
        listdata.append(data)
        print(listdata)
    elif menu == 2:
        print(listdata)
        index=int(input('수정할 인덱스를 입력:'))
        if index > len(listdata)-1:
            print('없는 인덱스')
        else:
            value=input('수정할 값을 입력:')
            listdata.pop(index)
            listdata.insert(index,value)
            print(listdata)
    elif menu == 3:
        print(listdata)
        index=int(input('삭제할 인덱스를 입력:'))
        listdata.pop(index)
        print(listdata)
