#include <iostream>

using namespace std;

int score;
//Total points = 50 and Passing rate is 70% = 35
int total_points = 50;
int passing_score = 35;

int main()
{
    cout << "Enter you score: ";
    cin >> score;
    cout << "Score: " << score << "/50" << endl;

    if (score>=passing_score && score<=total_points)
    {
        cout << "Passed!" << endl;
        cout << "Congratulations on passing the exam!" << endl;
    }
    else if (score<passing_score && score>=0)
    {
        cout << "Failed!" << endl;
        cout << "You have to study further!" << endl;
    }
    else if (score>50)
    {
        cout << "Invalid!" << endl;
    }
    else if (score<0)
    {
        cout << "Invalid!" << endl;
    }

    return 0;
}
