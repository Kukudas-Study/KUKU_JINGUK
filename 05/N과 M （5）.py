n,m = map(int,input().split())
numbers = sorted(list(map(int, input().split())))

nlist = []

def dfs():
    if len(nlist)==m:
        print(' '.join(map(str,nlist)))
        return
    
    for i in numbers:
        if i not in nlist:
            nlist.append(i)
            dfs()
            nlist.pop()
            
dfs()
