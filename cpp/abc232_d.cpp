#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
using ll = long long;
int H, W;
vector<vector<int>> memo;
vector<vector<char>> C;

ll dfs(int i, int j) {
    if (memo[i][j] != -1) return memo[i][j];
    ll ans1 = 0, ans2 = 0;
    bool hit = false;
    if (i + 1 < H && C[i + 1][j] != '#') {
        hit = true;
        ans1 = 1 + dfs(i + 1, j);
    }
    if (j + 1 < W && C[i][j + 1] != '#') {
        hit = true;
        ans2 = 1 + dfs(i, j + 1);
    }
    if (hit) return memo[i][j] = max(ans1, ans2);
    return 1;
}

void print() {
    for (auto i : C) {
        for (auto j : i) cout << j;
        cout << endl;
    }
    return;
}

int main() {
    cin >> H >> W;
    C.resize(H, vector<char>(W));
    memo.resize(H, vector<int>(W, -1));
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            cin >> C[i][j];
        }
    }
    cout << dfs(0, 0) << endl;
    return 0;
}