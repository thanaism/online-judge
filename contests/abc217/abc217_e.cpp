#include <iostream>
#include<queue>
#include<vector>
#include<functional>

using namespace std;

int main(){
	int Q;
	cin>>Q;
	queue<int> q;
	priority_queue<int,vector<int>,greater<int>> p;
	for(int i=0;i<Q;i++){
		int c,x;
		cin>>c;
		if(c==1){
			cin>>x;
			q.push(x);
		}
		if(c==2){
			if(p.empty()){
				cout<<q.front()<<endl;
				q.pop();
			}else{
				cout<<p.top()<<endl;
				p.pop();
			}
		}
		if(c==3){
			while(!q.empty()){
				p.push(q.front());
				q.pop();
			}
		}
	}
	return 0;
}