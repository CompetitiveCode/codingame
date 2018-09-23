//Answer to Temperatures in C++

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n,k=10000,l,m=10000; // the number of temperatures to analyse
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        int t; // a temperature expressed as an integer ranging from -273 to 5526
        cin >> t; cin.ignore();
        l=t;
        if(t<0)
        {
            l*=-1;
        }
        if(m>=l)
        {
            m=l;
            if(t==(k*-1)&&t<0)
            {
                k=k;
            }
            else
            {
                k=t;
            }
        }
    }
    if(k==10000)
    {
        k=0;
    }
    
    cout << k << endl;
}