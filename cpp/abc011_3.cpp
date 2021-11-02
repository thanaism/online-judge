#include<bits/stdc++.h>
using namespace std;
int main(){
	int n;
	cin>>n;
	vector<int> ns(3);
	for(int i=0;i<3;i++)cin>>ns[i];
	int cnt=100;
	while(cnt--){
		n-=3;
		bool flg=true;
		while(flg){
			flg=true;
			for(int i=0;i<3;i++)if(ns[i]==n){
				flg=false;break;
			}
			n++;
		}
	}
	
	cout<<((n<=0)?"YES":"NO")<<endl;
}