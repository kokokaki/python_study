

height = float(input('신장: '))

if height >= 140:
    age = int(input('나이: '))
    if age >= 8:
        print('놀이기구에 탑승할 수 있습니다.')
    else:
        print('나이가 8세 미만이라서 놀이기구에 탑승할 수 없습니다.')
else:
    print('키가 140cm미만이라서 놀이기구에 탑승할 수 없습니다.')