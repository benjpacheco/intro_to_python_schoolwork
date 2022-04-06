//Name:  Benyir J Pacheco
//Email:  benyir.pacheco60@myhunter.cuny.edu.
//Date:  May 13, 2020
#include <iostream>
using namespace std;

int main()
{  
    int i;
    float d, num;
    cout << "Enter a starting amount: " << endl;
    cin >> num;
    d = num * 2;
    i = 1;
    while (num < d)
    {
        cout << "Year " << (i++) << " " <<(num=num+num*0.1) << endl;
        
    }
    return 0;
}