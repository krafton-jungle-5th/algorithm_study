#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int n, m;
vector<int>v;
vector<int>v1;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> n;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		v.push_back(x);
	}
	cin >> m;
	for (int i = 0; i < m; i++) {
		int y;
		cin >> y;
		v1.push_back(y);
	}
	sort(v.begin(), v.end());
	for (int i = 0; i < v1.size(); i++) {
		if (binary_search(v.begin(), v.end(), v1[i])) {
			cout << 1 << "\n";
		}
		else {
			cout << 0 << "\n";
		}
	}
}
