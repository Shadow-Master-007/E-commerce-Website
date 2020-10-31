g={}
def dfs(s):
    global g
    global vis
    vis[s]=1
    print (s)
    for i in g[s]:
        if vis[i]==0:
            dfs(i)            

n=int(input("Enter no. of users: "))
m=int(input("Enter no. of friend connections(1-1): "))

print("Enter connections:")
for i in range(m):
    u,v=map(int,input().split())
    if u in g.keys():
        g[u].append(v)
    else:
        g[u]=[]
        g[u].append(v)
    if v in g.keys():
        g[v].append(u)
    else:
        g[v]=[]
        g[v].append(u)

print("DFS Tree:")
vis = [0 for i in range(n+1)]
dfs(1)
