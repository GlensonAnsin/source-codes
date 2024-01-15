#include <iostream>
using namespace std;

float hours_worked, dollar_exchange_rate = 58.63, hourly_rate = 2.60, salary_in_USD, salary_in_PHP;

int main ()
{
    cout << "Hours Worked: ";
    cin >> hours_worked;
    cout << endl;

    salary_in_USD = hours_worked * hourly_rate;
    cout << "Salary (USD): USD " << salary_in_USD << endl;
    cout << endl;

    salary_in_PHP = dollar_exchange_rate * salary_in_USD;
    cout << "Salary (PHP): PHP " << salary_in_PHP << endl;

    return 0;
}
