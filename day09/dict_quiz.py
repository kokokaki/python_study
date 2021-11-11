
word_dict = {}

print('[영어 단어장 만들기]')
print('- 종료하시려면 영단어에 "그만"을 입력하세요!')

while True:
    eng = input('\n영단어: ')

    if eng == '그만':
        print('종료합니다.')
        break

    if eng not in word_dict:
        kor = input('뜻: ')
        word_dict[eng] = kor;
    else:
        print('이미 등록된 단어입니다.')
        continue

print('\n ***** 단어장 *****')
for word in word_dict:
    print(f'# {word} : {word_dict[word]}')