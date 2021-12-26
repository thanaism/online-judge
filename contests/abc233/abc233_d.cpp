#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;
using ll = long long;

ll solve1(ll N, ll K, vector<ll> A) {
    // 先にCounterを作って、使ったら減らしていく
    unordered_map<ll, ll> mp;
    // mp[0]++;
    mp[A[0]]++;
    for (int i = 1; i < N + 1; i++) {
        A[i] += A[i - 1];
        mp[A[i]]++;
    }
    ll ans = 0;
    for (auto i : A) {
        mp[i]--;
        ans += mp[i + K];
    }
    return ans;
}

ll solve2(ll N, ll K, vector<ll> A) {
    // 自分より左のものだけを順次Counterに加えていく
    unordered_map<ll, ll> mp;
    ll ans = 0;
    for (int i = 1; i < N + 1; i++) {
        A[i] += A[i - 1];
    }

    // イテレータを使う練習
    // for (auto it = ++A.begin(); it != A.end(); it++) {
    //     auto pre = it - 1;
    //     mp[*pre]++;
    //     ans += mp[*it - K];
    // }

    // インデックスを使ったほうがシンプル
    for (int i = 1; i < N + 1; i++) {
        mp[A[i - 1]]++;
        ans += mp[A[i] - K];
    }
    return ans;
}

int main() {
    // input
    ll N, K;
    cin >> N >> K;
    vector<ll> A(N + 1);
    for (int i = 0; i < N; i++) cin >> A[i + 1];

    ll ans1 = solve1(N, K, A);
    ll ans2 = solve2(N, K, A);
    if (ans1 == ans2) cout << ans2 << endl;

    return 0;
}