#include <iostream>
#include <cstring>
using namespace std;
int dp[10002][1000];
int n,m;
int arr[10002];
int dfs(int x,int y){
    if(x > n)return -1;
    else if(x == n){
        if(y == 0)return 0;
        return -1;
    }
    if(y == m)return dfs(x+m,0);
    if(dp[x][y] !=-1)return dp[x][y];
    dp[x][y]=0;
    int ret1 = dfs(x+1,y+1);
    int ret2 = dfs(x+1,max(y-1,0));
    if(ret1!=-1)dp[x][y] = ret1 + arr[x];
    if(ret2 !=-1)dp[x][y] = max(dp[x][y], ret2);
    return dp[x][y];
}
int main() {
    // 여기에 코드를 작성해주세요.
    cin >> n >> m;
    for(int i=0;i<n;i++)cin >> arr[i];
    memset(dp, -1, sizeof dp);
    cout << dfs(0,0);
    return 0;
}