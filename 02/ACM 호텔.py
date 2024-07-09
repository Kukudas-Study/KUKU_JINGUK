T = int(input())
for _ in range(T):
    H,W,N = map(int,input().split())
    # 층수와 손님수가 같을때 
    if N%H==0:
        # 층수는 결국 높이
        floor = H
        # 방번호는 사람 수 에서 층수 나눈값
        room = N // H
    else:
        # 층수와 손님수가 같지않을때는 나누고 남는값
        floor = N % H
        # 방번호는 나눈값에 +1
        room = N // H + 1

    print(floor*100+room)
