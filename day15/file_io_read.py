

file_path = 'D:/isec_spring1/py_study/아무말.txt'

try:
    f = open(file_path, 'r', encoding='utf-8')
    data = f.read()
    print(data)
except:
    print('파일 로드 실패!')
finally:
    f.close()


print('=' * 40)
try:
    f = open(file_path, 'r', encoding='utf-8')
    while True:
        str = f.readline()
        if len(str) == 0: break
        print(str, end='')
except:
    print('파일 로드 실패!')
finally:
    f.close()