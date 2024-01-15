#include <iostream>
using namespace std;

int total_hours_worked;
float hourly_rate = 150.02;
float gross_salary;
//Deductibles: SSS 12%, PhilHealth 4%, Pag-IBIG 2%
//Total Deductibles: 18%
float total_deduction;
float net_salary;

int main()
{
    cout << "Total Hours Worked:";
    cin >> total_hours_worked;

    cout << endl;

    cout << "Hourly Rate: 150.02 pesos" << endl;

    cout << endl;

    gross_salary = total_hours_worked * hourly_rate;
    cout << "Gross Salary: " << gross_salary << " pesos" << endl;

    cout << endl;

    cout << "Deductibles: SSS 12%, PhilHealth 4%, Pag-IBIG 2% > Total: 18%" << endl;

    cout << endl;

    total_deduction = gross_salary * 0.18;
    cout << "Total Deduction: " << total_deduction << " pesos" << endl;

    cout << endl;

    net_salary = gross_salary - total_deduction;
    cout << "Net Salary: " << net_salary << " pesos" << endl;

    return 0;
}
