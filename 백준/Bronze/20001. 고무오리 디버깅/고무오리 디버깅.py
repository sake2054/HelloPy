q = 0
while True:
    i = input()
    if i == "고무오리 디버깅 시작" :
        pass
    elif i == "고무오리 디버깅 끝" :
        break
    elif i == "문제" :
        q += 1
    elif i == "고무오리" :
        if q == 0 :
            q += 2
        else :
            q += -1
if q == 0 :
    print("고무오리야 사랑해")
else :
    print("힝구")