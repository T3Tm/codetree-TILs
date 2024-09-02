#include <bits/stdc++.h>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;cin >> n;
    vector<char> board(n);
    for(auto&v:board)cin >> v;
    char criteria = board.back();
    int cnt{1};

    int i{};
    while(i<n && board[i] == criteria)i++;
    for(;i<n;i++){
        while(i < n && board[i]!=criteria)i++;
        while(i<n && board[i] == criteria)i++;
        cnt++;
    }
    cout << cnt;
    return 0;
}