
#include <iostream>

using namespace std;

int factorial(int num) {
	if (num == 0)
		return 1;
	else
		return num * factorial(num - 1);
}

int main() {

	int n;
	
	cin >> n;
	
	int fact = factorial(n);

	cout << fact;
	
}

