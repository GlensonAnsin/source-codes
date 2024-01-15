#include <iostream>

using namespace std;

int main()
{
    char meal;
    float cash;
    float change;
    float voucher = .15; //15%
    float total_amount;

    cout << "Choose your meal!" << endl;
    cout << "[A] Thai Basil Chicken with Iced Tea - PHP 250.00 \n[B] Creamy Mushroom Chicken with Iced Tea - PHP 300.00 \n[C] Southern Style Chicken Fillet - PHP 150.00" << endl;
    cout << endl;
    cout << "Enter you meal: ";
    cin >> meal;

    switch (meal)
    {
    case 'A':
        cout << "Meal A: Thai Basil Chicken with Iced Tea - PHP 250.00" << endl;
        total_amount = (250.00) - 250.00 * voucher;
        cout << "Total Amount: PHP " << total_amount << " (15% voucher applied)" << endl;
        cout << "Cash: PHP ";
        cin >> cash;
        change = cash - total_amount;
        cout << "Change: PHP " << change << endl;
        break;
    case 'B':
        cout << "Meal B: Creamy Mushroom Chicken with Iced Tea - PHP 300.00" << endl;
        total_amount = (300.00) - 300.00 * voucher;
        cout << "Total Amount: PHP " << total_amount << " (15% voucher applied)" << endl;
        cout << "Cash: PHP ";
        cin >> cash;
        change = cash - total_amount;
        cout << "Change: PHP " << change << endl;
        break;
    case 'C':
        cout << "Meal C: Southern Style Chicken Fillet - PHP 150.00" << endl;
        total_amount = (150.00) - 150.00 * voucher;
        cout << "Total Amount: PHP " << total_amount << " (15% voucher applied)" << endl;
        cout << "Cash: PHP ";
        cin >> cash;
        change = cash - total_amount;
        cout << "Change: PHP " << change << endl;
        break;
    default:
        cout << "Error! Please input correctly." << endl;
        break;
    }

    return 0;
}
