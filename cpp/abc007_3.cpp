#include <iostream>
#include <queue>
#include <vector>

using namespace std;
#define rep(i, n) for(int i=0; i<(int)(n); i++)
int main(){
	int R,C;
	cin>>R>>C;
	int sy,sx;
	cin>>sy>>sx;
	sy--;sx--;
	int gy,gx;
	cin>>gy>>gx;
	gy--;gx--;
	vector<vector<char>> c(R,vector<char>(C));
	vector<vector<int>> dist(R,vector<int>(C,-1));
	rep(i,R)rep(j,C){
		cin>>c[i][j];
	}
	vector<int> dx = {1,0,-1,0};
	vector<int> dy = {0,-1,0,1};
	queue<pair<int,int>> q;
	q.push(pair<int,int>(sy,sx));
	dist[sx][sy]=0;
	while(!q.empty()){
		int x=q.front().first;
		int y=q.front().second;
		q.pop();
		rep(d,4){
			int nx,ny;
			nx=x+dx[d];
			ny=y+dy[d];
			// if(nx<0 || nx>=R || ny<0 || ny>=C)continue;
			if(c[nx][ny]=='#' || dist[nx][ny]!=-1)continue;
			dist[nx][ny]=dist[x][y]+1;
			q.push(pair<int,int>(nx,ny));
		}
	}
	cout<<dist[gy][gx]<<endl;
}