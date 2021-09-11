#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;
using ll = long long;
using vll = vector<ll>;
using vvll = vector<vll>;

#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define all(obj) (obj).begin(),(obj).end()

int main() {
	string S,T;
	cin>>S>>T;
	unordered_map<char,char> mp_a,mp_b;
	bool ok=true;
	rep(i,S.size()){
		char s=S[i],t=T[i];
		if(mp_a.count(s))if(mp_a[s]!=t)ok=false;
		if(mp_b.count(t))if(mp_b[t]!=s)ok=false;
		mp_a[s]=t;mp_b[t]=s;
	}
	if(ok)puts("Yes");
	else puts("No");
	return 0;
}