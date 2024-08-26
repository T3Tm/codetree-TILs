#include <bits/stdc++.h>
using namespace std;
int arrn[1002],arrm[1002];
int dp[1002][1002];
const int INF = 0x3f3f3f3f;
int n,m;

int dfs(int depth, int index){
    if(depth == min(n,m))return 0;
    if(index >= max(n,m))return INF;
    if (dp[depth][index]!=INF)return dp[depth][index];
    
    auto idx = lower_bound(arrm + index, arrm + m, arrn[depth]) - arrm;
    for(int i=index;i<idx;i++){
        dp[depth][index] = min(dp[depth][index], dfs(depth+1,i+1) + abs(arrn[depth] - arrm[i]));
    }
    return dp[depth][index];
}
int main() {
    cin >> n >> m;
    memset(dp, 0x3f, sizeof dp);
    for(int i=0;i<n;i++)cin >> arrn[i];
    for(int j=0;j<m;j++)cin >> arrm[j];

    sort(arrn,arrn+n, greater<int>());
    sort(arrm,arrm+m, greater<int>());
    cout << dfs(0,0);

    return 0;

}