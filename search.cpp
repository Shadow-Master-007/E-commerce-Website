#include<bits/stdc++.h>

const int N = 1e5+10;

using namespace std;

vector<int> graph[N];
int vis[N]={0};

void dfs(int s)
{
  cout<<s<<", ";
  vis[s]=1;
  for (int v: graph[s])
  {
    if (vis[v]==0)
      dfs(v);
  }
}

int main()
{
  int n,m,x,y;
  cin>>n>>m;
  for (int i=0;i<m;i++)
  {
    cin>>x>>y;
    graph[x].push_back(y);
    graph[y].push_back(x);
  }
  cout<<"Nodes in DFS search: ";
  for (i=1;i<=n;i++)
  {
    if (vis[i]==0)
      dfs(i);
  }
  return 0;
}
