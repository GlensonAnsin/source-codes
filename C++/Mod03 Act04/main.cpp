#include <iostream>

using namespace std;

int main()
{
    int midterm_grade;
    cout << "Input Midterm Grade: ";
    cin >> midterm_grade;

    if (midterm_grade>=97 && midterm_grade<=100)
    {
        cout << "Numerical Value: 1.00" << endl;
        cout << "Description: Excellent" << endl;
    }
    else if (midterm_grade>=94 && midterm_grade<=96)
    {
        cout << "Numerical Value: 1.25" << endl;
        cout << "Description: Excellent" << endl;
    }
    else if (midterm_grade>=91 && midterm_grade<=93)
    {
        cout << "Numerical Value: 1.50" << endl;
        cout << "Description: Very Good" << endl;
    }
    else if (midterm_grade>=88 && midterm_grade<=90)
    {
        cout << "Numerical Value: 1.75" << endl;
        cout << "Description: Very Good" << endl;
    }
    else if (midterm_grade>=85 && midterm_grade<=87)
    {
        cout << "Numerical Value: 2.00" << endl;
        cout << "Description: Above Average" << endl;
    }
    else if (midterm_grade>=82 && midterm_grade<=84)
    {
        cout << "Numerical Value: 2.25" << endl;
        cout << "Description: Above Average" << endl;
    }
    else if (midterm_grade>=79 && midterm_grade<=81)
    {
        cout << "Numerical Value: 2.50" << endl;
        cout << "Description: Average" << endl;
    }
    else if (midterm_grade>=76 && midterm_grade<=78)
    {
        cout << "Numerical Value: 2.75" << endl;
        cout << "Description: Average" << endl;
    }
    else if (midterm_grade==75)
    {
        cout << "Numerical Value: 3.00" << endl;
        cout << "Description: Passing" << endl;
    }
    else if (midterm_grade>=72 && midterm_grade<=74)
    {
        cout << "Numerical Value: 3.25" << endl;
        cout << "Description: Conditional" << endl;
    }
    else if (midterm_grade>=69 && midterm_grade<=71)
    {
        cout << "Numerical Value: 3.50" << endl;
        cout << "Description: Conditional" << endl;
    }
    else if (midterm_grade>=66 && midterm_grade<=68)
    {
        cout << "Numerical Value: 3.75" << endl;
        cout << "Description: Failed" << endl;
    }
    else if (midterm_grade==65)
    {
        cout << "Numerical Value: 4.00" << endl;
        cout << "Description: Failed" << endl;
    }
    else if (midterm_grade>=0 && midterm_grade<=64)
    {
        cout << "Numerical Value: 5.00" << endl;
        cout << "Description: Failed" << endl;
    }
    else
    {
        cout << "Invalid Grade!" << endl;
        cout << "Please input again!" << endl;
    }

    return 0;

}
