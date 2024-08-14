#include <iostream>
#include <set>
using namespace std;

int main(){
    int n,m;cin >> n >>m ;
    set<int,greater<int>> nums;
    for(int i=0,a;i<n;i++){
        cin >> a;
        nums.insert(a);
    }
    
    for (int i=0;i<m;i++){
        int num;cin >> num;
        auto iter = nums.lower_bound(num);
        if(iter!=nums.end()){
            cout << *iter << '\n';
            nums.erase(iter);
        }else cout << "-1\n";
    }
    return 0;
}