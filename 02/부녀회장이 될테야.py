T = int(input())

for _ in range(T):
    floor = int(input())
    rooms = int(input())

    # 주어진 호 수 만큼 배열을 만들고 1부터 1씩늘어나게 채워줌 => 0층
    numbers = [x for x in range(1, rooms+1)]
    # 주어진 층 수 만큼 반복
    for _ in range(floor):
        # 0층 배열의  각 인덱스의 값에 전 인덱스의 값을 더해줌
        for i in range(1,rooms):
            numbers[i] += numbers[i-1]
    # -1 인덱스로 마지막 값을 출력
    print(numbers[-1])
