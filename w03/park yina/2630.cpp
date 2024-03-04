#include<iostream>
#include<algorithm>
#define MAX 128+7
using namespace std;
int map[MAX][MAX];
int white;
int n;
int blue;
void input() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> map[i][j];
		}
	}
}
bool check(int n, int x, int y) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (map[x + i][y + j] != map[x][y])
				return false;
		}
	}
	return true;
}

void solve(int n,int x,int y) {
	if (check(n, x, y)) {
		if (map[x][y] == 1)blue++;
		else white++;
	}
	else {
		n /= 2;
		solve(n, x, y);
		solve(n, x + n, y);
		solve(n, x, y + n);
		solve(n, x + n, y + n);
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	input();
	solve(n, 0, 0);
	cout << white << "\n" << blue;
	return 0;
}
