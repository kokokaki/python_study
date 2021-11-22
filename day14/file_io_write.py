

# 파일 저장 기능

# 내가 저장할 폴더 위치
dir_name = 'D:/isec_spring1/py_study/'

# 저장할 파일명
file_name = input('파일명: ')

# 파일 저장 기능
text = '안녕안녕 메롱메롱 방가방가!! \n하하호호호'

try:
    # 파일입출력을 실행하는 내장함수 open(path, mode)
    # mode: w - 파일저장, r - 파일로드
    f = open(dir_name + file_name + '.txt', 'w')

    f.write(text)
    print('파일 저장 성공!')
except: 
    print('파일 저장 실패!')
finally:
    f.close() # 메모리 자원반납