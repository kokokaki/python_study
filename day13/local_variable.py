
'''
# 지역 변수
- 지역변수란 함수 내부에서 만들어진 변수를 말합니다.
- 지역변수는 함수 내부에서만 사용할 수 있으며, 함수호출이 종료되면
  메모리에서 자동제거됩니다.
'''

def info():
    word = '안녕' # 지역변수
    print(word)
    for c in word:
        print(c)

def greeting():
    word = 'hello'
    print(word)




info()
greeting()
