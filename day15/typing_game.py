
import random as r
import time as t  # 시간과 날짜를 제어하는 모듈

# 사운드 출력 모듈
import winsound

# 텍스트 데이터를 읽어서 저장시킬 리스트
word_list = []

#==== 함수 정의부 =====#

# 메모장에 있는 단어를 읽어들이는 함수
def read_words():

    file_path = 'D:/isec_spring1/py_study/resource/word.txt'

    try:
        f = open(file_path, 'r')
        while True:
            w = f.readline()
            if len(w) == 0: break
            # \n제거
            word_list.append(w.strip())   
    except:
        print('파일 로드 실패')
    finally:
        f.close()

# 문제 출제 처리 함수
def assign_question(q_list):

    ok_cnt = 0

    for n in range(len(q_list)):
        print(f'\n# Question *{n + 1}')
        print(f'> {q_list[n]}')
        answer = input('> ')

        if answer == q_list[n]:
            print('\nRight!!')
            ok_cnt += 1

            # 소리 재생
            winsound.PlaySound(
                'D:/isec_spring1/py_study/sound/good.wav'
                , winsound.SND_FILENAME
                )
        else:
            print('\nWrong!!')
            winsound.PlaySound(
                'D:/isec_spring1/py_study/sound/bad.wav'
                , winsound.SND_FILENAME
                )
    
    return ok_cnt

# 결과 판정 함수
def show_result(cnt, game_time):
    print('\n과연 결과는??? ㄷㄱㄷㄱㄷㄱㄷㄱ')

    t.sleep(3)

    if cnt >= 3:
        print('합격!!')
    else:
        print('불합격!!')
    
    print(f'총 게임시간: {round(game_time, 2)}초, 정답 개수: {cnt}개')


# 게임 시작 함수
def start():
    read_words()
    input('Ready?? Press Enter Key!')

    # 5문제를 저장할 리스트
    # 랜덤으로 5문제를 뽑아야 함
    q_list = r.sample(word_list, 5)
    
    start = t.time() 

    # 문제를 출제하는 함수
    ok_cnt = assign_question(q_list)

    end = t.time() 

    # 결과 판정 함수
    show_result(ok_cnt, end-start)




#### 메인 실행부 #####
if __name__ == '__main__':
    start()