n,m = map(int,input().split())
numbers = sorted(list(map(int, input().split())))

nlist = []

def dfs(s):
    if len(nlist)==m:
        print(' '.join(map(str,nlist)))
        return
    
    for i in range(s , len(numbers)):
            nlist.append(numbers[i])
            dfs(i)
            nlist.pop()
            
dfs(0)
