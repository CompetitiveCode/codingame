//Answer to The Descent in C++

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int k=0,l=0;
    while (1) {
        for (int i = 0; i < 8; i++) {
            int mountainH; // represents the height of one mountain.
            cin >> mountainH; cin.ignore();
            if(mountainH>k)
            {
                k=mountainH;
                l=i;
            }
        }

        cout << l << endl; // The index of the mountain to fire on.
        k=0;
        l=0;
    }
}