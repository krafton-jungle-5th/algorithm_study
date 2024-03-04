#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<cstring>
#define MAX 1001
using namespace std;
bool visit[MAX];
vector<int>v[MAX];
void dfs(int x) {
	visit[x] = true;//방문을 체크하여준다.
	cout << x << " ";
	for (int i = 0; i < v[x].size(); i++) {
		int y = v[x][i];
		if(!visit[y])
		dfs(y);
	}
}
void bfs(int x) {
	queue<int> q;
	q.push(x);
	visit[x] = true;
	while (!q.empty()) {
		int current = q.front();
		q.pop();
		cout << current << " ";
		for (int i = 0; i < v[current].size(); i++) {
			int neighbor = v[current][i];
			if (!visit[neighbor]) {
				q.push(neighbor);
				visit[neighbor] = true;
			}
		}
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int x, y;
	int n = 0; int m = 0; int z = 0;
	cin >> n >> m >> z;
	fill(visit, visit + MAX, false);

	for (int i = 0; i < m; i++) {
		cin >> x >> y;
		v[x].push_back(y);
		v[y].push_back(x);
	}
	for (int i = 1; i <= n; i++) {
		sort(v[i].begin(), v[i].end());
	}

	dfs(z);
	cout<<"\n";
	memset(visit, false, sizeof(visit));
	bfs(z);
	return 0;
}
