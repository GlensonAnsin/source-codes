#include <iostream>

using namespace std;

int main()
{
    char meal;
    float cash;
    float change;
    float amount;
    float total_amount;
    int chances = 100;
    char add;

    cout << "Choose your meal!" << endl;
    cout << "[A] Thai Basil Chicken with Iced Tea - PHP 250.00 \n[B] Creamy Mushroom Chicken with Iced Tea - PHP 300.00 \n[C] Southern Style Chicken Fillet - PHP 150.00" << endl;
    cout << endl;

    while (chances!=0)
    {
        cout << "Enter your meal: ";
        cin >> meal;

        switch (meal)
        {
        case 'A':
            cout << "Meal A: Thai Basil Chicken with Iced Tea" << endl;
            amount = 250.00;
            cout << "Amount: PHP " << amount << endl;
            total_amount += amount;
            cout << "Add another order (Y or N): ";
            cin >> add;
            if (add=='Y')
            {
                chances--;
            }
            else if (add=='N')
            {
                chances=0;
            }
            cout << endl;
            break;
        case 'B':
            cout << "Meal B: Creamy Mushroom Chicken with Iced Tea" << endl;
            amount = 300.00;
            cout << "Amount: PHP " << amount << endl;
            total_amount += amount;
            cout << "Add another order (Y or N): ";
            cin >> add;
            if (add=='Y')
            {
                chances--;
            }
            else if (add=='N')
            {
                chances=0;
            }
            cout << endl;
            break;
        case 'C':
            cout << "Meal C: Southern Style Chicken Fillet" << endl;
            amount = 150.00;
            cout << "Amount: PHP " << amount << endl;
            total_amount += amount;
            cout << "Add another order (Y or N): ";
            cin >> add;
            if (add=='Y')
            {
                chances--;
            }
            else if (add=='N')
            {
                chances=0;
            }
            cout << endl;
            break;
        default:
            cout << "Invalid! Please input correctly." << endl;
            break;
        }
    }

    cout << "Total Amount: PHP " << total_amount << endl;
    cout << "Cash: PHP " ;
    cin >> cash;
    change = cash - total_amount;
    cout << "Change: PHP " << change << endl;

    return 0;
}
