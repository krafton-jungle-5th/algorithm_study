#include<iostream>
#include<math.h>
#define MAX 1005
#define FAST ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
using namespace std;
int cnt;
int num;
bool prime(int n) {
	if (n == 1)return false;
	int k = (int)sqrt(n);
	for (int i = 2; i <= k; i++) {
		if (n % i == 0)return false;
	}
	return true;
}
int main() {
	FAST;
	cin >> num;
	for (int i = 0; i < num; i++) {
		int input = 0;
		cin >> input;
		if (prime(input))cnt++;
	}
	cout << cnt;
	return 0;
}