#include <iostream>
#include <set>
using namespace std;

int main() {
	int l,q;
	cin>>l>>q;
	set<int> s;
	s.insert(0);
	s.insert(l);
	for (int i=0;i<q;i++) {
		int c,x;
		cin>>c>>x;
		if (c==1) {
			s.insert(x);
			continue;
		}
		auto right = s.lower_bound(x);
		auto left = prev(right);
		cout<<*right-*left<<endl;
	}
}