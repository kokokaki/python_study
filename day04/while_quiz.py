

# x ~ y 까지의 총합
x = int(input('정수1: '))
y = int(input('정수2: '))

total = 0
n = x

while n <= y:
    total += n
    n += 1

print(f'{x}~{y}까지의 총합: {total}')