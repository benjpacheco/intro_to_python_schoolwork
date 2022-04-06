//Name:  Benyir J Pacheco
//Email:  benyir.pacheco60@myhunter.cuny.edu.
//Date:  May 12, 2020
#include <iostream>
using namespace std;

int main()
{
    int age;
    cout << "Enter an age: " << endl;
    cin >> age;
    while (age <= 0)
    {
        cout << "Entered a negative number.\n";
        cout << "Enter an age: ";
        cin >> age;
    }
    cout << "You entered your age as: " << age;
 

    return 0;
}