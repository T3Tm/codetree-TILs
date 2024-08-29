#include <bits/stdc++.h>
using namespace std;

const int MX = 5000 * 200 + 2;
const int ROOT = 1;
int unused1 = 2;
int unused2 = 2;
int nxt1[MX][26];
int nxt2[MX][26];

bool chk1[MX];
bool chk2[MX];

inline int c2i(const char& v){
    return v - 'a';
}

int travel(int cur, int nxt[][26], bool chk[], int depth){
    int ret{};
    if(chk[cur])ret = depth;//일단 이정도는 벌었음
    for(int i=0;i<26;i++){//26칸 중에서 돌아보고 travel 호출
        if(nxt[cur][i])
            ret = max(travel(nxt[cur][i],nxt, chk, depth + 1), ret);
    }
    return ret;
}
void insert(const string& s, int nxt[][26], int& unused, bool chk[]){
    int cur = ROOT;
    for(auto &v: s){
        if(nxt[cur][c2i(v)] == 0){
            nxt[cur][c2i(v)] = unused++;
        }
        cur = nxt[cur][c2i(v)];
    }
    chk[cur] = true;
}
int find(const string&s, int nxt[][26], bool chk[]){
    //s를 접두어로 가지는 제일 긴 문자열 찾기
    int ret{};//제일 긴 문자열이 0이다.
    int cur = ROOT;
    for(int idx{}; idx< s.size();idx++){//
        auto &v = s[idx];
        if(!nxt[cur][c2i(v)]){//해당하는 곳에 있으니까 그 쪽으로 들어가기
            return 0;//불가능
        }
        if(idx + 1 == (int)s.size() && chk[cur]){//마지막에서 하나 적을 때 있으면 이걸로
            ret = s.size() - 1;
        }
        cur = nxt[cur][c2i(v)];
    }
    //여기까지 왔다는 것은 해당하는 곳에 도착을 했다는 것이고
    if (chk[cur]){//이 단어가 있다는 것을 확인
        //해당 곳에서 제일 긴 곳을 찾아야 된다..
        int depth = travel(cur, nxt, chk, 0);//
        //제일 깊은 거 알려줌
        return max(ret, depth);
    }
    return ret;//없음
}

int main(){
    cin.tie(0) -> ios::sync_with_stdio(0);
    int n;cin >> n;
    vector<string> arr;
    for(int i=0;i<n;i++){
        string tmp;cin >> tmp;
        arr.push_back(tmp);
        insert(tmp, nxt1, unused1, chk1);
        reverse(tmp.begin(),tmp.end());
        insert(tmp, nxt2, unused2, chk2);
    }

    int result{};
    for(auto &st: arr){
        //앞으로 붙었을 때 최고 이려면 내 문자열이 xxx 일 때 asdfadsfdsa xxx의 형태여야 함
        //즉 뒤에 붙는 아이들은 
        result = max(result,(int)st.size() + find(st, nxt2, chk2));
        reverse(st.begin(), st.end());//내가 뒤에 붙는 다면?
        result = max(result,(int)st.size() +  find(st, nxt1, chk1));
    }
    cout << result;
    return 0;
}