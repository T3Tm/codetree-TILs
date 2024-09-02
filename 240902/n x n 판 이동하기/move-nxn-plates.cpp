#include <bits/stdc++.h>
using namespace std;
int n;
long long dp[102][102];
int board[102][102];
const long long INF = 0x3f3f3f3f3f3f3f3f;
long long dfs(int x,int y){
    if (x == n || y == n)return INF;
    if(x  == n-1 && y == n-1)return 1;
    if(dp[x][y]!=INF)return dp[x][y];
    int val = board[x][y];
    dp[x][y] = 0;
    long long r = dfs(x+val,y);
    long long v = dfs(x,y+val);
    if(r != INF)dp[x][y] += r;
    if (v != INF)dp[x][y] += v;
    return dp[x][y];
}
int main() {
    memset(dp,0x3f, sizeof dp);cin >> n;
    for(int i=0;i<n;i++)for(int j=0;j<n;j++)cin >> board[i][j];
    cout << dfs(0,0);
    return 0;
}