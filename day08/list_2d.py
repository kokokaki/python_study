

# 2차원 리스트 - 리스트 내부의 데이터가 또다시 리스트인 형태

# 우리반 학생 5명의 1과목점수를 저장
# 리스트가 1개필요
# 우리반 학생 5명의 4과목점수를 저장
my_class = [ 
    [100, 96, 85, 95],
    [88, 76, 92, 91], 
    [100, 100, 100, 100], 
    [23, 34, 41, 12], 
    [0, 0, 100, 100] 
]
print(type(my_class))
print(len(my_class))
print(my_class[0])
print(my_class[1][2])

print(type(my_class[3]))
print(type(my_class[0][2]))

print('=' * 40)
stuNum = 1 # 학생 번호

student_avg_list = [] # 학생들의 평균들을 저장할 리스트

kor_sum = 0 # 국어점수 총점
for li in my_class:

    kor_sum += li[0]

    each_total = 0 # 1명의 총점을 저장
    for n in li:
        each_total += n
    each_avg = each_total / len(li) # 1명의 평균 

    student_avg_list.append(each_avg)        

    print('{}번째 학생 총점: {}점, 평균: {:.2f}점'.format(stuNum, each_total, each_avg))

    stuNum += 1



# 반평균
avg_total = 0 # 평균 총합
for avg in student_avg_list:
    avg_total += avg
class_avg = avg_total / len(student_avg_list)
print('우리반 평균: {:.2f}점'.format(class_avg))

# 국어점수 평균
kor_avg = kor_sum / len(my_class)
print('국어점수 평균: {:.2f}점'.format(kor_avg))