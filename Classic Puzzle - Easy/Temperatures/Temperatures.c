//Answer to Temperatures in C

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main()
{
    int n,k=10000,l,m=10000; // the number of temperatures to analyse
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int t; // a temperature expressed as an integer ranging from -273 to 5526
        scanf("%d", &t);
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
    
    printf("%d\n",k);

    return 0;
}