#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
using ll = long long;

int main() {
    string S;
    cin >> S;
    ll d1 = ll(S[0] - '0');
    ll d2 = ll(S[2] - '0');
    cout << d1 * d2 << endl;
    return 0;
}