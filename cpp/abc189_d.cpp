#include <iostream>
using namespace std;
int main(){
	int N;
	cin>>N;
	long long ans=1;
	for(int i=1;i<=N;i++){
		string s;
		cin>>s;
		if(s=="OR")ans+=1ll<<i;
	}
	cout<<ans<<endl;
}