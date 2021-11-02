

kor = int(input('국어: '))
eng = int(input('영어: '))
math = int(input('수학: '))

avg = (kor + eng + math) / 3
# avg = round(avg, 2)
print('당신의 평균점수: {:.2f}점'.format(avg))

if avg >= 60:
    print('이번 시험에 통과하셨습니다.')
else:
    print('재수강 대상자입니다.')
print('열공하세요!')