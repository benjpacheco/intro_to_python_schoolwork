#include <iostream>        //The built-in library for input/output
using namespace std;


int main() {
	
	  for (int i = 0; i < 6; i++) {
		       for (int j = 1; j < i; j++) {
			          if (j % 2 == 0)
				                cout << "0";
			          else
				                cout << "1";
			
		}
		     cout << endl;
		
	}
	
		
   return 0;
	
}