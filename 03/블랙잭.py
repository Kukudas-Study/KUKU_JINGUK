from itertools import combinations
N, M = map(int,input().split())
numbers = list(map(int, input().split()))
maxsum = 0
# 콤비네이션 써서 숫자 3개씩 만듭니다
for nthree in combinations(numbers,3):
	# 숫자 3개의 합을 구합니다
    numsum = sum(nthree)
# 합이 M보다 작거나 같을때
    if numsum <= M:
	    # maxsum 보다 클때
        if maxsum < numsum:
		# maxnum은 3개숫자 합! 젤 큰값이 maxnum 됨
            maxsum = numsum
 
print(maxsum)
	
