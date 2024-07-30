n,m = list(map(int,input().split()))

list = []

def dfs():
    if len(list)==m:
        print(' '.join(map(str,list)))
        return
    
    for i in range(1,n+1):
        if i not in list:
            list.append(i)
            dfs()
            list.pop()
            
dfs()
