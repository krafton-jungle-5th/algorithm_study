#include<iostream>
#include<algorithm>
#include<vector>
#define MAX 9
using namespace std;
int n, m;
vector<int> num;
bool visit[MAX];
void permutation(int cnt) {
	if (cnt == m) {
		for (int i = 0; i < m; i++) {
			cout << num[i] << " ";
		}
		cout << "\n";
		return;
	}
	for (int i = 1; i <= n; i++) {
		if (!visit[i]) {
			visit[i] = true;
			num.push_back(i);
			permutation(cnt + 1);
			num.pop_back();
			visit[i] = false;
		}
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> n >> m;
	permutation(0);
	return 0;
}
