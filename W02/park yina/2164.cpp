#include<iostream>
#include<stack>
#include<queue>
#define FAST ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
using namespace std;
queue<int>q;
int n;
int main() {
	FAST;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		q.push(i);
	}
	while (q.size()!=1) {
		q.pop();
		int f = q.front();
		q.push(f);
		q.pop();

	}
	cout << q.front();
	return 0;

}
