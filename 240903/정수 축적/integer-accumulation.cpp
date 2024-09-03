#include <iostream>
#include <cstring>
using namespace std;
int dp[10002][1000];
int n,m;
int arr[10002];
int dfs(int x,int y){
    if(x>n)return -1e9;
    if(x == n){
        if (y==0)return 0;
        return -1e9;
    }
    if(y == m){
        return dfs(x+m,0);
    }
    if(dp[x][y] !=-1)return dp[x][y];
    dp[x][y]=max(dfs(x+1,y+1)+arr[x],dfs(x+1,max(y-1,0)));
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