#include <iostream>
using namespace std;

int main()
{
    string names[5];
    string search_name;

    cout << "Enter 5 names: " << endl;
    for (int ctr = 0; ctr < 5; ctr++)
    {
        cin >> names[ctr];
    }
    cout << endl;
    cout << "Search for a name: " << endl;
    cin >> search_name;
    cout << endl;
    for (int ctr = 0; ctr < 5; ctr++)
    {
        if (names[ctr] == search_name)
        {
            cout << "Name found!" << endl;
            cout << endl;
        }
        else
        {
            cout << "Name NOT found!" << endl;
            cout << endl;
        }
    }
    return 0;
}
