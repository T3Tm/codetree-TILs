#include <bits/stdc++.h>
using namespace std;

int main(){
	cin.tie(0) -> ios::sync_with_stdio(0);
	int n;cin >> n;
	unordered_map<int,int>log;
	int result{};
	for(int i=0;i<n;i++){
		int a,b;cin >> a >> b;
		if(log.count(a)){
			result += log[a]!=b;
		}
		log[a] = b;
	}
	cout << result;
	return 0;
}