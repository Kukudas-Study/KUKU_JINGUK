M = int(input())
money = 1000-M
coins = [500,100,50,10,5,1]
answer = 0
# 코인 큰값부터 돌면서
for i in coins :
    # 해당 코인 사용한 갯수 더함
    answer += money//i
    # 거스름돈 줘야하는것 에서 해당 코인값 빼줌
    money %=i
    
print(answer)
