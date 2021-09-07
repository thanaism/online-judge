#include<iostream>
#include<vector>
#include<queue>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;

#define rep(i,n) for(int i=0;i<(int)(n);i++)

int main() {
	int N,M;
	cin>>N>>M;
	vi A(M);
	vi B(M);
	rep(i,M)cin>>A[i]>>B[i];
	vvi peer(N);
	rep(i,M){
		peer[A[i]-1].push_back(B[i]-1);
		peer[B[i]-1].push_back(A[i]-1);
	}
	rep(k,N){
		vi dist(N,-1);
		dist[k]=0;
		queue<int> q;
		q.push(k);
		while(!q.empty()){
			int i=q.front();q.pop();
			for(auto j:peer[i]){
				if(dist[j]==-1){
					dist[j]=dist[i]+1;
					q.push(j);
				}
			}
		}
		int ans=0;
		rep(i,N)if(dist[i]==2)ans+=1;
		cout<<ans<<endl;
	}
	return 0;
}