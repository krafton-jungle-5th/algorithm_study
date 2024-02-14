#include<iostream>
using namespace std;
int solve(int n) {
	if (n == 0||n==1)return n;
	else return (solve(n - 1) + solve(n - 2));
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int input = 0;
	cin >> input;
	cout<<solve(input);
}
