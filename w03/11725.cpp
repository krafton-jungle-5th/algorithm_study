#include<iostream>
#include<vector>
#include<queue>
using namespace std;
int n;
struct Node
{
	vector<int>child;
	int parent = 0;
};
vector<Node>tree;
queue<int>q;
void bfs() {
	while (!q.empty()) {
		int cur = q.front();
		q.pop();
		for (int i = 0; i < tree[cur].child.size(); i++) {
			int nc = tree[cur].child[i];
			if (tree[cur].parent == nc)continue;//만약 자식이 이미 방문 노드인데 부모이면 탐색 불필요
			q.push(nc);
			tree[nc].parent = cur;//자 그럼 이제 다음번 트리의 노드에 대한 부모는 현재의 노드가 되기 때문

		}
	}
}
int main() {
	ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	cin >> n;
	tree.resize(n + 1);
	tree[1].parent = -1;
	for (int i = 1; i < n; i++) {
		int a = 0; int b = 0;
		cin >> a >> b;
		tree[a].child.push_back(b);
		tree[b].child.push_back(a);
	}
	q.push(1);
	bfs();
	for (int i = 2; i <= n; i++) {
		cout << tree[i].parent << "\n";
	}

	return 0;
}
