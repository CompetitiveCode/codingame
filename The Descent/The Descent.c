//Answer to The Descent in C

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main()
{
    int k=0,l=0;
    while (1) {
        for (int i = 0; i < 8; i++) {
            int mountainH; // represents the height of one mountain.
            scanf("%d", &mountainH);
            if(mountainH>k)
            {
                k=mountainH;
                l=i;
            }
        }

        printf("%d\n",l); // The index of the mountain to fire on.
        k=0;
        l=0;
    }

    return 0;
}