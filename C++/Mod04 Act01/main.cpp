#include <iostream>
using namespace std;

float add(float a, float b)
{
    float sum;
    sum = (a + b);
    return(sum);
}
float subtract(float a, float b)
{
    float difference;
    difference = (a - b);
    return(difference);
}
float multiply(float a, float b)
{
    float product;
    product = (a * b);
    return(product);
}
float divide(float a, float b)
{
    float quotient;
    quotient = (a / b);
    return(quotient);
}

int main()
{
    float answer;
    float a;
    float b;

    cout << "First number: ";
    cin >> a;
    cout << "Second number: ";
    cin >> b;
    cout << endl;

    answer = add(a, b);
    cout << "Sum" << endl;
    cout << "Answer: " << answer << endl;
    cout << endl;

    answer = subtract(a, b);
    cout << "Difference" << endl;
    cout << "Answer: " << answer << endl;
    cout << endl;

    answer = multiply(a, b);
    cout << "Product" << endl;
    cout << "Answer: " << answer << endl;
    cout << endl;

    answer = divide(a, b);
    cout << "Quotient" << endl;
    cout << "Answer: " << answer << endl;
    cout << endl;

    return 0;
}
