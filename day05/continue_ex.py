

for x in range(10):
    if x % 2 == 0:
        continue
    print(x, end=' ')
print('\n반복문 종료!')

print('=' * 40)

for student in [90, 87, 99, 20, 43, 92, 76]:
    if student > 60: continue
    print(student)