n,k = map(int,input().split())
# false 배열
a = [False] * (n+1)
# 지워진 수
cat = 0

for i in range(2,n+1):
    for j in range(i,n+1,i):
        if a[j] == False:
            # 지움
            a[j] = True
            cat += 1
            # k번째 지워지면 출력
            if cat == k:
                print(j)
                break
