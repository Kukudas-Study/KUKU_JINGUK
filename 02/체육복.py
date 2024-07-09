def solution(n, lost, reserve):
    # 여벌 체육복 가저온 학생이 잃어버리면 빌려줄수 없기 때문에!
    # 중복되는 수 삭제
    lost2 = set(lost)-set(reserve)
    reserve2 = set(reserve)-set(lost)
    #잃어버린 학생의
    for a in lost2:
        #앞에 여벌의 체육복을 가져온 학생이있다면 빌려줌
        if a-1 in reserve2:
            reserve2.remove(a-1)
            # 아니면 뒤에 여벌의 체육복을 가져온 학생이 있다면 빌려줌
        elif a+1 in reserve2:
            reserve2.remove(a+1)
        # 앞뒤로 없다면 빌려줄수 없으므로 전체학생수에서 1 빼줌
        else: n-=1
    return n
