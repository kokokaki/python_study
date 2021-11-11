
# 딕셔너리를 이용한 팝송 가사의 알파벳 카운팅
# {a: 38, b:22, ..., z:12}

lyrics = '''
Hey Jude don't make it bad
Take a sad song and make it better
Remember to let her into your heart
Then you can start to make it better
Hey Jude don't be afraid
You were made to go out and get her
The minute you let her under your skin
Then you begin to make it better
And anytime you feel the pain
hey Jude refrain
Don't carry the world upon your shoulders
For well you know that
it's a fool who plays it cool
By making his world a little colder
Nah nah nah nah nah nah nah nah nah
Hey Jude don't let me down
You have found her now go and get her
Remember to let her into your heart
Then you can start to make it better
So let it out and let it in hey Jude begin
You're waiting for someone to perform with
And don't you know that
it's just you hey Jude you'll do
The movement you need
is on your shoulder
Nah nah nah nah nah
nah nah nah nah yeah
Hey Jude don't make it bad
Take a sad song and make it better
Remember to let her under your skin
Then you'll begin to make it
Better better better better better better
ohhhhhhhhhhhhhhhhhhhh
Nah nah nah nah nah nah
nah nah nah hey Jude
Nah nah nah nah nah nah
nah nah nah hey Jude
Nah nah nah nah nah nah
nah nah nah hey Jude
Nah nah nah nah nah nah
nah nah nah hey Jude
Nah nah nah nah nah nah
nah nah nah hey Jude
Nah nah nah nah nah nah
nah nah nah hey Jude
Nah nah nah nah nah nah
nah nah nah hey Jude
Nah nah nah nah nah nah
nah nah nah hey Jude
Nah nah nah nah nah nah
nah nah nah hey Jude
'''

# 알파벳과 그 횟수를 저장할 딕셔너리 생성
alphabet = {}

# 노래가사를 한글자씩 반복순회한다
for c in lyrics:
    
    # 가사에서 알파벳이 아닌 특수문자나 공백은 관심대상이 아님
    # 건너뛰어야 함
    if not c.isalpha(): 
        continue

    # 만약에 알파벳이라면 대소문자를 통일한다.
    c = c.lower()

    # 현재 등장한 알파벳이 처음 등장했다면 1이라는 카운트와 함께
    # 딕셔너리에 추가
    if c not in alphabet:
        alphabet[c] = 1
    else:
        alphabet[c] += 1

# 결과 출력
# print(alphabet)

# 정렬을 하려면 리스트를 이용합니다.
keylist = []
for k in alphabet:
    keylist.append(k)

keylist.sort()
# print(keylist)

print('======= 노래가사 알파벳 빈도 ========')
for k in keylist:
    count = alphabet[k]
    print(f'# {k} => {count}')

