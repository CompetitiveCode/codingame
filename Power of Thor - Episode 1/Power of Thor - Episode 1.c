//Answer to Power of Thor - Episode 1 in C

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main()
{
    int lightX; // the X position of the light of power
    int lightY; // the Y position of the light of power
    int initialTX; // Thor's starting X position
    int initialTY; // Thor's starting Y position
    scanf("%d%d%d%d", &lightX, &lightY, &initialTX, &initialTY);

    while (1) {
        int remainingTurns; // The remaining amount of turns Thor can move. Do not remove this line.
        scanf("%d", &remainingTurns);

        if(initialTX>lightX&&initialTY==lightY)
        {
            printf("W\n");
            initialTX--;
        }
        else if(initialTX<lightX&&initialTY==lightY)
        {
            printf("E\n");
            initialTX++;
        }
        else if(initialTX==lightX&&initialTY>lightY)
        {
            printf("N\n");
            initialTY--;
        }
        else if(initialTX==lightX&&initialTY<lightY)
        {
            printf("S\n");
            initialTY++;
        }
        else if(initialTX<lightX&&initialTY<lightY)
        {
            printf("SE\n");
            initialTX++;
            initialTY++;
        }
        else if(initialTX<lightX&&initialTY>lightY)
        {
            printf("NE\n");
            initialTX++;
            initialTY--;
        }
        else if(initialTX>lightX&&initialTY<lightY)
        {
            printf("SW\n");
            initialTX--;
            initialTY++;
        }
        else if(initialTX>lightX&&initialTY>lightY)
        {
            printf("NW\n");
            initialTX--;
            initialTY--;
        }

    }

    return 0;
}