//Answer to Power of Thor - Episode 1 in C++

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int lightX; // the X position of the light of power
    int lightY; // the Y position of the light of power
    int initialTX; // Thor's starting X position
    int initialTY; // Thor's starting Y position
    cin >> lightX >> lightY >> initialTX >> initialTY; cin.ignore();

    while (1) {
        int remainingTurns; // The remaining amount of turns Thor can move. Do not remove this line.
        cin >> remainingTurns; cin.ignore();

        if(initialTX>lightX&&initialTY==lightY)
        {
            cout << "W" << endl;
            initialTX--;
        }
        else if(initialTX<lightX&&initialTY==lightY)
        {
            cout << "E" << endl;
            initialTX++;
        }
        else if(initialTX==lightX&&initialTY>lightY)
        {
            cout << "N" << endl;
            initialTY--;
        }
        else if(initialTX==lightX&&initialTY<lightY)
        {
            cout << "S" << endl;
            initialTY++;
        }
        else if(initialTX<lightX&&initialTY<lightY)
        {
            cout << "SE" << endl;
            initialTX++;
            initialTY++;
        }
        else if(initialTX<lightX&&initialTY>lightY)
        {
            cout << "NE" << endl;
            initialTX++;
            initialTY--;
        }
        else if(initialTX>lightX&&initialTY<lightY)
        {
            cout << "SW" << endl;
            initialTX--;
            initialTY++;
        }
        else if(initialTX>lightX&&initialTY>lightY)
        {
            cout << "NW" << endl;
            initialTX--;
            initialTY--;
        }

    }
}