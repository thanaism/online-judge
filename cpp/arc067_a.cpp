#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N;
	cin>>N;
	vector<int> d(N+1,1);
	for(int i=1;i<=N;i++){
		int x=i;
		for(int j=2;j*j<=i;j++){
			while(x%j==0){
				d[j]+=1;
				x/=j;
			}
		}
		if(x!=1)d[x]+=1;
	}
	long long ans=1;
	long long MOD=1000000007;
	for(int i=2;i<=N;i++){
		ans*=d[i];
		ans%=MOD;
	}
	cout<<ans<<endl;
}