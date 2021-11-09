
tvxq = ['영웅재중', '최강창민', '유노윤호', '시아준수', '믹키유천']

while True:
    print('\n수정전:', tvxq)
    old_name = input('수정할 이름을 입력: ')

    if old_name in tvxq:
        new_name = input('새로운 이름: ')
        tvxq[tvxq.index(old_name)] = new_name
        print('수정 완료!')
        print('\n수정후:', tvxq)
        break
    else:
        print('그런 멤버는 없어~~')