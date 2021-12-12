#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <vector>

using namespace std;
using ll = long long;

vector<ll> A;
map<ll, ll> memo;

ll ceil(ll x, ll y) { return (x + y - 1) / y; }

ll dfs(ll x, ll beg) {
    // すでにメモされている場合：.end()は最後の要素の「次」を指す
    if (memo.find(x) != memo.end()) return memo[x];
    // 最大額の硬貨を使う場合：繰り上がりはない
    if (beg == (ll)A.size() - 1) return x / A.back();
    // 0円なら0枚を返す
    if (x == 0) return 0;
    // 今の硬貨
    ll crr = A[beg];
    // 次の硬貨：最大額の硬貨はこの時点でreturn済
    ll nxt = A[beg + 1];
    // 次の額で割ったあまりを今の額で割る
    // X = 87, A = (1, 10, 100)の場合：
    // 87 % 10 / 1 = 7
    // X = 87, A = (1, 4, 28)の場合：
    // 87 % 4 / 1 = 3
    // 今の硬貨をちょうど使う場合の枚数
    ll r = x % nxt / crr;
    // ちょうど支払う場合：今回使った枚数を足して再帰を進める
    // x / nxt * nxt = 87 / 10 * 10 = 80
    ll ans = dfs(x / nxt * nxt, beg + 1) + r;
    // 支払う硬貨が0枚以外の場合：お釣りをもらうパターン
    // ceil(x, nxt) * nxt = 90
    // nxt / crr - r = 10 / 1 - 7 = 3
    if (r) ans = min(ans, dfs(ceil(x, nxt) * nxt, beg + 1) + (nxt / crr - r));
    return memo[x] = ans;
}

ll calc(ll n, ll x) {
    vector<ll> cnt(n);
    for (int i = n - 1; i > -1; i--) {
        cnt[i] = x / A[i];
        x %= A[i];
        if (i - 1 >= 0) A[i] /= A[i - 1];
    }

    ll INF = 1ll << 60;
    vector<vector<ll>> dp(n + 1, vector<ll>(2, INF));
    dp[0][0] = 0;

    for (int i = 0; i < n; i++) {
        ll nxt = INF;
        if (i != n - 1) nxt = A[i + 1];

        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + cnt[i]);
        if (cnt[i] + 1 < nxt)
            dp[i + 1][0] = min(dp[i + 1][0], dp[i][1] + cnt[i] + 1);

        dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + (nxt - cnt[i] - 1));
        if (cnt[i] > 0)
            dp[i + 1][1] = min(dp[i + 1][1], dp[i][0] + (nxt - cnt[i]));
    }

    return dp[n][0];
}

int main() {
    ll N, X;
    cin >> N >> X;
    A.resize(N);
    for (int i = 0; i < N; i++) cin >> A[i];
    ll ans1 = dfs(X, 0);
    ll ans2 = calc(N, X);
    assert(ans1 == ans2);
    cout << ans2 << endl;
}