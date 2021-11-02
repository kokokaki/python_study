

print('*** 음식을 선택하세요 ***')
print('[짜장면, 볶음밥, 카레, 돈까스]')

food = input('> ')

if food == '짜장면':
    print('{}의 가격은 4500원입니다.'.format(food))
elif food == '볶음밥':
    print('{}의 가격은 6500원입니다.'.format(food))
elif food == '카레':
    print('{}의 가격은 5500원입니다.'.format(food))
elif food == '돈까스':
    print('{}의 가격은 7500원입니다.'.format(food))
else:
    print(f'{food}는(은) 없는 메뉴입니다.')