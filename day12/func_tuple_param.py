
def add2(n1, n2):
    return n1 + n2

def add3(n1, n2, n3):
    return n1 + n2 + n3

# n개의 정수를 전달하면 총합을 구해주는 함수
def add_all(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def add_all2(*numbers):
    numbers = list(numbers)
    print(type(numbers))
    total = 0
    for n in numbers:
        total += n
    return total

#############################################

result = add_all((10, 20, 30))
print(result)

result2 = add_all2(100, 300, 100)
print(result2)

