#전자레인지
#A,B,C 바튼을 적절히 사용해서 조리시간 T를 만족하는 최소 횟수 구하기

time = int(input())
A_Btn = 300
B_Btn = 60
C_Btn = 10
A_total = 0
B_total = 0
C_total = 0

#time이 A로 나누어 떨어질 때, 몫이 B로 나누어 떨어질 때 , A B C 조합으로 안 나누어 떨어질 때 구분

while True:
    if time % A_Btn == 0:
        A_total = time // A_Btn
        B_total = 0
        C_total = 0
        print(A_total, B_total, C_total)
        break
    else:
        A_total = time // A_Btn
        time = time % A_Btn
        if time % B_Btn == 0:
            B_total = time // B_Btn
            time = time % B_Btn
            C_total = 0
            print(A_total, B_total, C_total)
            break
        else:
            B_total = time // B_Btn
            time = time % B_Btn
            C_total = time // C_Btn
            time = time % C_Btn
            if time == 0:
                print(A_total, B_total, C_total)
                break
            else:
                print(-1)
                break



