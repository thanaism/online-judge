#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    long long N, D, L, R;
    vector<pair<long long, long long>> LR;
    long long INF = 1ll << 60;
    cin >> N >> D;
    for (int i = 0; i < N; i++) {
        cin >> L >> R;
        LR.emplace_back(L, R);
    }
    sort(LR.begin(), LR.end(),
         [](pair<long long, long long>& a, pair<long long, long long>& b) {
             return a.second < b.second;
         });
    long long ans = 0, x = -INF;
    for (auto it = LR.begin(); it != LR.end(); it++) {
        if (x + D - 1 < it->first) ans++, x = it->second;
    }
    cout << ans << endl;
    return 0;
}