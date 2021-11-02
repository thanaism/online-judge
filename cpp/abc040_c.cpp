#include<iostream>
#include<vector>
using namespace std;
using ll = long long;
using vll = vector<ll>;
#define rep(i,n) for(ll i=0;i<(ll)(n);i++)
int main() {
	int N;
	cin>>N;
	vll a(N);
	rep(i,N)cin>>a[i];
	ll INF=1ll<<60;
	vll dp(110000,INF);
	dp[0]=0;
	rep(i,N+1){
		dp[i+1]=min(dp[i+1],dp[i]+abs(a[i+1]-a[i]));
		dp[i+2]=min(dp[i+2],dp[i]+abs(a[i+2]-a[i]));
	}
	cout<<dp[N-1]<<endl;
}