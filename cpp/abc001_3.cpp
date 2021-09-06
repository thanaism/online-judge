#include <iostream>
using namespace std;

const char *dir[]={"N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"};
int wnd[]={15, 93, 201, 327, 477, 645, 831, 1029, 1245, 1467, 1707, 1959, 12000};

int main()
{
    int deg, dis;
    cin>>deg>>dis;
    deg=(deg+112)%3600/225;
    int w=0;
    while(dis>=wnd[w]) ++w;
    if(w==0) cout<<"C 0\n";
    else cout<<dir[deg]<<' '<<w<<'\n';
    return 0;
}
