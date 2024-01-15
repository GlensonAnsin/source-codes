#include <iostream>
using namespace std;

//VARIABLES DECLARATION
float price_per_kg;
int number_of_kg;
float total_price;

int main()
{
    cout << "Enter price per kilogram:";
    cin >> price_per_kg;

    cout << "Enter number of kilograms:";
    cin >> number_of_kg;

    total_price = price_per_kg * number_of_kg;

    cout << "Total price:" << total_price;

    return 0;
}
