#include <iostream>
using namespace std;

int n, d, x, a;

int main() {
    cin >> n >> d >> x;
    for (int i = 1; i <= n; i++){
        cin >> a;
        int cnt = (d-1)/a+1;
        x+=cnt;
    }
    cout << x << endl;
    return 0;
}