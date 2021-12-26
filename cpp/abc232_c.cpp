#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
using ll = long long;

int main() {
    int N, M;
    cin >> N >> M;
    if (M == 0) {
        cout << "Yes" << endl;
        return 0;
    }
    vector<pair<int, int>> AB;
    for (int i = 0; i < M; i++) {
        int A, B;
        cin >> A >> B;
        AB.emplace_back(make_pair(A, B));
    }
    vector<pair<int, int>> CD;
    for (int i = 0; i < M; i++) {
        int C, D;
        cin >> C >> D;
        CD.emplace_back(make_pair(C, D));
    }
    vector<int> v;
    for (int i = 1; i <= 8; i++) v.emplace_back(i);
    do {
        bool ok = true;
        for (int i = 0; i < M; i++) {
            bool tmp = false;
            for (int j = 0; j < M; j++) {
                int a = AB[i].first, b = AB[i].second;
                int c = CD[j].first, d = CD[j].second;
                int nc = v[c - 1];
                int nd = v[d - 1];
                if (nc > nd) swap(nc, nd);
                if (a == nc && b == nd) {
                    tmp = true;
                    break;
                }
            }
            if (!tmp) {
                ok = false;
                break;
            }
        }
        if (ok) {
            cout << "Yes" << endl;
            return 0;
        }
    } while (next_permutation(v.begin(), v.end()));
    cout << "No" << endl;

    return 0;
}