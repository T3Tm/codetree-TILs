#include <bits/stdc++.h>
using namespace std;
int n,m;
int arrn[1002];
int arrm[1002];
int tmp[1002];
int main() {
    cin.tie(0) -> sync_with_stdio(0);
    cin >> n >> m;
    for(int i=0;i<n;i++){
        cin >> arrn[i];
        tmp[i] = arrn[i];
    }
    for(int j=0;j<m;j++){
        cin >> arrm[j];
    }
    if(m > n){
        for(int i=0;i<m;i++){
            arrn[i] = arrm[i];
        }
        for(int i=0;i<n;i++){
            arrm[i] = tmp[i];
        }
        swap(n,m);
    }
    sort(arrn,arrn+n);
    sort(arrm,arrm+m);
    
    int ret{};

     int start = 0;
     for(int i=0;i<m;i++){
         int end = n - (m - i - 1);//[start, end]일 때 arr[i]와 가장 가까운 값

         int gap = 1e6 ;
         int indx = -1;
         for(int j= start; j < end;j++){
             if(abs(arrn[j] - arrm[i]) < gap){
                 gap = abs(arrn[j] - arrm[i]);
                 indx = j;
             }
         }
         start = indx+1;
         ret += gap;
     }

     cout << ret;   
    return 0;
}