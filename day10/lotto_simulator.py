
import random


win = []
bonus_num = 0

while len(win) < 6:
    num = random.randint(1, 45)
    if num not in win:
        win.append(num)

while True:
    bonus = random.randint(1, 45)
    if bonus not in win:
        bonus_num = bonus
        break                 

# 앞에서부터 1등당첨횟수 ~ 5등횟수 + 꽝횟수
prize = [0,0,0,0,0,0]

paper = 0
my_lotto = [] 

while True:

    cnt = 0 # 일치번호 횟수
    num = random.randint(1, 45)

    if num not in my_lotto:
        my_lotto.append(num)

    if len(my_lotto) == 6:
        paper += 1

        for n in my_lotto:
            if n in win:
                cnt += 1           

        if cnt == 6:
            prize[0] += 1
        elif cnt == 5:
            if bonus_num in my_lotto:
                prize[1] += 1
            else:
                prize[2] += 1
        elif cnt == 4:
            prize[3] += 1
        elif cnt == 3:
            prize[4] += 1
        else:
            prize[5] += 1

        print("로또 %d장 구매..." % paper)                

        my_lotto.clear()         

        if prize[0] == 1:
            break

print("="*50)

print("당첨 횟수    당첨시 수령액(세후,평균)    누적 당첨금        당첨 확률")

print("1등: %d번    %d원                  %d원                %.6f%%" 
        % (prize[0],1500000000,prize[0]*1500000000,(prize[0]/paper)*100))
print("2등: %d번    %d원                      %d원                %.6f%%" 
        % (prize[1],40000000,prize[1]*40000000,(prize[1]/paper)*100))
print("3등: %d번    %d원                        %d원                %.6f%%" 
        % (prize[2],1000000,prize[2]*1000000,(prize[2]/paper)*100))
print("4등: %d번    %d원                          %d원        %.6f%%" 
        % (prize[3],50000,prize[3]*50000,(prize[3]/paper)*100))
print("5등: %d번    %d원                          %d원        %.6f%%" 
        % (prize[4],5000,prize[4]*5000,(prize[4]/paper)*100))
print("꽝: %d번        0원                          0원                %.6f%%" 
        % (prize[5],(prize[5]/paper)*100))
print("="*50)

use = paper*1000
print("누적 사용 금액: %d원" % use)
summ = prize[0]*1500000000 + prize[1]*40000000 + prize[2]*1000000 + prize[3]*50000 + prize[4]*5000

print("누적 당첨금 총합: %d원" % summ)

subt = summ-use
print("순이익: %d원" % subt)
print("수익률: %.2f%%" % ((subt / use)*100))
print("="*50)  










