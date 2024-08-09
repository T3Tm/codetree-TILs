#include <bits/stdc++.h>
using namespace std;

int main(){
    cin.tie(0) -> ios::sync_with_stdio(0);
    int n;cin >> n;
    set<int>nums;
    for(int i=0;i<2 * n;i++){
        int num;cin >> num;
        nums.insert(num);
    }

    int left = 0, right = *prev(nums.end());
    while(left<=right){
        int mid = (left + right) >> 1;
        set<int>temp;
        for(auto &v:nums)temp.insert(v);

        bool flag = true;
        for(auto &v:temp){//
            auto it = temp.lower_bound(v + mid);
            if(it == temp.end()){
                flag = false;
                break;
            }
            temp.erase(it);
        }
        if(flag){
            left = mid + 1;
        }else{//불가능하다면 차이를 줄이자
            right = mid -1;
        }
    }
    cout << right;
    return 0;
}