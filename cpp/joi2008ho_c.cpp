#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
using ll = long long;
using vll = vector<ll>;
using vvll = vector<vll>;

#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define all(obj) (obj).begin(),(obj).end()

int main() {
    int N, M;
    cin >> N >> M;
    vll P(N+1);
    rep(i,N)cin >> P[i];
    vll V;
    V.push_back(0);
    V.push_back(M);
    rep(i,N+1)rep(j,N+1){
        ll pt = P[i] + P[j];
        if(pt<M)V.push_back(pt);
    }
    sort(V.begin(),V.end());
    ll ans;
    for(auto v:V){
        if(v==M)break;
        ll ok = 0;
        ll ng = V.size() - 1;
        while(abs(ng-ok)>1){
            ll mid = (ok+ng)/2;
            if(v + V[mid]<M){
                ok = mid;
            }else{
                ng = mid;
            }
        }
        if(ans<v+V[ok])ans = v+V[ok];
    }
    cout << ans << endl;
    return 0;
}