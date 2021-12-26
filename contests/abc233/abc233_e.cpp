#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
using ll = long long;

int main() {
    string X;
    cin >> X;

    vector<ll> a;
    for (auto c : X) {
        a.emplace_back(ll(c - '0'));
    }
    for (auto it = ++a.begin(); it != a.end(); it++) {
        *it += *(it - 1);
    }
    ll up;
    string s;
    for (auto it = a.rbegin(); it != a.rend(); it++) {
        ll d = *it + up;
        up = d / 10;
        s.push_back('0' + d % 10);
    }
    if (up > 0) s.push_back('0' + up);

    // for (auto c = s.rbegin(); c != s.rend(); c++) cout << *c;
    // cout << endl;
    reverse(s.begin(), s.end());
    cout << s << endl;
    return 0;
}