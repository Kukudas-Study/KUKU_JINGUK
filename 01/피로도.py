A,B,C,M = map(int, input().split())
hard = 0
work =0
# 24시간 24번반복
for i in range(24) :
    # 피로도가 M보다 높으면 포기
    if hard > M :
        print(0)
    else:
        # A만큼 피로도 더해도 M보다 작으면 일가능
        if hard +A<= M:
            hard += A
            work += B
        else:
            # 피로도 C만큼 감소 0보다 작아지면 그냥 0
            if hard - C >=0:
                hard -= C
            else:
                hard =0
print(work)
