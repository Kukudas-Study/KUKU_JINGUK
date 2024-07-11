def solution(brown, yellow):
    total = brown + yellow
    #x는 3부터 total 의 제곱근 까지 확인
    for x in range(3,int(total**0.5)+1):
        if total % x == 0:
            # x*y = total
            y = total // x
            #x-2 * y-2 = yellow의 값이 되는경우
            # -> brown의 테두리를 제외한 숫자
            if (x-2)*(y-2) == yellow:
                # x를 작은수부터 돌렸기 때문에 y를 가로로
                return [y,x]
    return []
             
