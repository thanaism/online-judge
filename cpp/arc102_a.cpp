#include <iostream>
using namespace std;
using ll = long long;

int main() {
	int N,K;
	cin>>N>>K;
	ll a=0,b=0;
	for(int i=1;i<=N;i++){
		if(i%K==0)a++;
		if(i%K==K/2)b++;
	}
	ll ans=a*a*a;
	if(K%2==0)ans+=b*b*b;
	cout<<ans<<endl;
}