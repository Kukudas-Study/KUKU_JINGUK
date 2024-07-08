def solution(n):
    # n값을 2로 나눈 몫 만큼 '수박' 곱해서 더해줌@
    # 홀수일때를 생각해 n%2 하여서 '수' 더해줌
    answer = '수박' * (n//2) + '수' * (n % 2)
    
    return answer
