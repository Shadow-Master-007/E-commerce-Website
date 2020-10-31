g={}
def bfs(s):
    global g
    global vis
    q=[]
    q.append(s)
    while len(q)!=0:
        v=q[0]
        vis[v]=1
        q.pop(0)
        for i in g[v]:
            if vis[i]==0:
                q.append(i)
    
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

print("BFS Tree:")
vis = [0 for i in range(n+1)]
bfs(1)
