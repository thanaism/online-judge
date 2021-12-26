#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
using ll = long long;

int main() {
    string S, T;
    cin >> S >> T;
    int n = S.size();
    for (int i = 0; i < 26; i++) {
        bool ok = true;
        for (int j = 0; j < n; j++) {
            int d = int(S[j] - 'a');
            char c = 'a' + ((d + i) % 26);
            if (c != T[j]) {
                ok = false;
                break;
            }
        }
        if (ok) {
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
    return 0;
}