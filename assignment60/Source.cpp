//Name:  Benyir J Pacheco
//Email:  benyir.pacheco60@myhunter.cuny.edu.
//Date:  May 13, 2020
#include <iostream>
using namespace std;

int main()
{
   
    int n,b,x;
    cout << "Enter a number: " << endl;
    cin >> n;
    if (n < 0)
    {
        cout << "1";
        x = 32 + n;
    }
    else
    {
        cout << "0";
        x = n;
    }
    b = 16;
    while (b > 0.5)
    {
        if (x >= b)
            cout << "1";
        else
            cout << "0";
       x = x%b;
       b = b / 2;
    }
    cout << "\n";
    return 0;
}