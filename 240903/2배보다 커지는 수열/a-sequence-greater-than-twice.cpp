#include <iostream>
using namespace std;
const int MOD = (int)1e9 + 7;
int dp[11][2001];
int main() {
    int n,m;cin >> n >> m;

    for(int i=1;i<=m;i++)dp[1][i] = 1;

    for(int i=2;i<=n;i++){
        for(int j=1;j<=m;j++){
            for(int z=1;z<=j/2;z++){
                dp[i][j] = (dp[i][j] + dp[i-1][z])%MOD;
            }
        }
    }
    int result{};
    for(int j=1;j<=m;j++){
        result = (result + dp[n][j])%MOD;
    }
    cout << result;
    return 0;
}