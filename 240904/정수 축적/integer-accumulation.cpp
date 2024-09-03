#include <iostream>

using namespace std;

int n, m; 
#define N_MAX (10'000 + 1)
#define M_MAX (1'000 +1)
int arr[N_MAX];
int dp[N_MAX][M_MAX][2];

int main() {
    cin>>n>>m;

    for(int i=1; i<=n; i++)
        cin>>arr[i];
    
    for(int i=1; i<=n; i++){
        int val = arr[i]; 
        dp[i][0][0] = max(dp[i][0][0], dp[i-1][0][0]);
        dp[i][0][0] = max(dp[i][0][0], dp[i-1][1][1]); 
        dp[i][0][0] = max(dp[i][0][0], dp[i-1][1][0]); 
        dp[i][0][1] = dp[i][0][0] = max(dp[i][0][0], dp[i][0][1]);  
        
        for(int j=1; j<=m; j++){
            dp[i][j][0] = max(dp[i][j][0], dp[i-1][j-1][0] + val); 
            
            if(j+1<=m){
                dp[i][j][1] = max(dp[i][j][1], dp[i-1][j+1][0]);
                dp[i][j][1] = max(dp[i][j][1], dp[i-1][j+1][1]); 
            }
            
            dp[i][j][1] = max(dp[i][j][0], dp[i][j][1]); 
        }
        // taking a break or not, # of fatigues, sum of integers
            
    }

    int ans =  max(dp[n][0][0], dp[n][0][1]);
    cout<<ans; 
    
    return 0;
}