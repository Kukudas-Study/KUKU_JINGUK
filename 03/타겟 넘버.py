def solution(numbers, target):
  # 재귀함수를 이용해 풀고자 함
    def targetNumber(index, sum):
      # numbers 인덱스 끝까지 가고
        if index == len(numbers):
          # sum 이 taget 이 되면 answer 값 더해주고 끝
            if sum==target:
                nonlocal answer
                answer+=1
            return
          # 인덱스 첫번째부터 돌면서 더하거나 뺴주기~
        targetNumber(index+1,sum+numbers[index])
        targetNumber(index+1,sum-numbers[index])
    answer = 0
    targetNumber(0,0)
    return answer
