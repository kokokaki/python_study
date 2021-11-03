

print('***** 점수 관리 프로그램 *****')
point = int(input('점수를 입력하세요: '))

if point >= 90:
    if point > 100:
        print('점수를 잘못 입력했습니다.')
    elif point >= 95:
        print('당신의 학점은 A+입니다.')
    else:
        print('당신의 학점은 A입니다.')
elif point >= 80:
    if point >= 85:
        print('당신의 학점은 B+입니다.')
    else:
        print('당신의 학점은 B입니다.')
elif point >= 70:
    print('당신의 학점은 C입니다.')
elif point >= 60:
    print('당신의 학점은 D입니다.')
else:
    print('당신의 학점은 F입니다.')