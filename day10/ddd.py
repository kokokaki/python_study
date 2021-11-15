
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

prz1 = 0
prz2 = 0
prz3 = 0
prz4 = 0
prz5 = 0
prz_no = 0
paper = 0
my_lotto = [] 

while True:

    cnt = 0
    num = random.randint(1, 45)

    if num not in my_lotto:
        my_lotto.append(num)

    if len(my_lotto) == 6:
        paper += 1

        for n in my_lotto:
            for w in win:
                if n == w:
                    cnt += 1           

        if cnt == 6:
            prz1 += 1
        elif cnt == 5:
            if bonus_num in my_lotto:
                prz2 += 1
            else:
                prz3 += 1
        elif cnt == 4:
            prz4 += 1
        elif cnt == 3:
            prz5 += 1
        else:
            prz_no += 1

        print("\n로또 %d장 구매..." % paper)                

        my_lotto.clear()         

        if prz1 == 1:
            break

print("="*50)

print("당첨 횟수    당첨시 수령액(세후,평균)    누적 당첨금        당첨 확률")

print("1등: %d번    %d원                  %d원                %.5f%%" 
        % (prz1,1500000000,prz1*1500000000,(prz1/paper)*100))
print("2등: %d번    %d원                      %d원                %.5f%%" 
        % (prz2,40000000,prz2*40000000,(prz2/paper)*100))
print("3등: %d번    %d원                        %d원                %.5f%%" 
        % (prz3,1000000,prz3*1000000,(prz3/paper)*100))
print("4등: %d번    %d원                          %d원        %.5f%%" 
        % (prz4,50000,prz4*50000,(prz4/paper)*100))
print("5등: %d번    %d원                          %d원        %.5f%%" 
        % (prz5,5000,prz5*5000,(prz5/paper)*100))
print("꽝: %d번        0원                          0원                %.5f%%" 
        % (prz_no,(prz_no/paper)*100))
print("="*50)

use = paper*1000
print("누적 사용 금액: %d원" % use)
summ = prz1*1500000000 + prz2*40000000 + prz3*1000000 + prz4*50000 + prz5*5000

print("누적 당첨금 총합: %d원" % summ)

subt = summ-use
print("순이익: %d원" % subt)
print("수익률: %.2f%%" % ((subt / use)*100))
print("="*50)  













