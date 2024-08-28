#include <bits/stdc++.h>
using namespace std;
const int MX = 32 * 150000 + 2;
int root = 1;
int unused = 2;
int nxt[MX][2];

void insert(vector<int>&s, int nxt[][2]){
    int cur = root;
    for(auto& v: s){
        if(nxt[cur][v] == 0){
            nxt[cur][v] = unused++;
        }
        cur = nxt[cur][v];
    }
}
int result;
void find(vector<int>&s){
    int cur = root;
    int num = 0;
    
    int value{};
    for(int i=0;i<32;i++){
        if(nxt[cur][s[i]^1]){
            cur = nxt[cur][s[i]^1];
            num += (s[i]^1) << (31 - i); 
        }else{
            cur = nxt[cur][s[i]];
            num += s[i] << (31 - i);
        }
        value += (s[i] << (31-i));
    }

    result = max(result, num ^ value);
}
int number[150001];
void to_binary(int n, vector<int>&v){
    for(int i=31;i>=0;i--){
        v[31-i] = (n & (1 << i)? 1 : 0);
    }
}
int main(){
    cin.tie(0) -> ios::sync_with_stdio(0);
    int n;cin >> n;
    for(int i=0;i<n;i++)cin >> number[i];
    vector<vector<int>>number_binary(n,vector<int>(32));

    for(int i{};i<n;i++){
        int num = number[i];
        to_binary(num, number_binary[i]);
        insert(number_binary[i], nxt);
    }

    for(int i{};i<n;i++){
        find(number_binary[i]);
    }
    cout << result;

    return 0;
}