// suplem07 코드
#include <iostream>
#include <vector>

using namespace std;

vector<pair<int, int>> ladders;
vector<int> origin_Route;
int n, m;

vector<vector<bool>> generate_Grid(const vector<pair<int, int>>& ldr) {
    vector<vector<bool>> tmp_Grid;
    int depth = 1;

    //최대 재귀 깊이를 알아낸다. b를 통해서
    for (const pair<int, int>& ladder : ldr)
        depth = max(depth, ladder.second);

    tmp_Grid.resize(n + 1, vector<bool>(depth + 1, false));

    //tmp가 행이여야 될 것 같은데
    for (const pair<int, int>& ladder : ldr)
        tmp_Grid[ladder.first][ladder.second] = true;
    
    return tmp_Grid;
}

vector<int> find_Route(const vector<pair<int, int>>& ldr) {
    vector<vector<bool>> grid = generate_Grid(ldr);
    vector<int> way;
    int depth = grid[1].size() - 1;

    for (int i = 1; i <= n; i++) {
        pair<int, int> pos = { i, 1 };
        while (true) {
            if (pos.second > depth) {
                way.push_back(pos.first);
                break;
            }

            if (pos.first != n && grid[pos.first][pos.second])
                pos.first++;
            else if (pos.first != 1 && grid[pos.first - 1][pos.second])
                pos.first--;

            pos.second++;
        }
    }

    return way;
}

bool is_The_Route(const vector<pair<int, int>>& ldr) { return find_Route(ldr) == origin_Route; }

void generate_Combination(vector<pair<int, int>>& tmp, int idx, int& answer, int depth) {
    if (idx > m) 
        return;

    if (is_The_Route(tmp)){
        answer = min(depth, answer);  
        return;
    }
    //6 , 9 , 11, 13
    tmp[depth] = ladders[idx];
    generate_Combination(tmp, idx + 1, answer, depth+1);
    tmp[depth] = {0,0};
    generate_Combination(tmp, idx + 1, answer, depth);
}

void solve() {
    vector<pair<int, int>> tmp_ladders (m);
    int answer = (int)ladders.size();

    generate_Combination(tmp_ladders, 0, answer,0);
    
    cout << answer << endl;
}

int main() {
    cin >> n >> m;

    ladders.resize(m);
    for (pair<int, int>& ladder : ladders)
        cin >> ladder.first >> ladder.second;

    origin_Route = find_Route(ladders);

    solve();

    return 0;
}