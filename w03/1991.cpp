#include<iostream>
#include<vector>
#define MAX 27
using namespace std;
int n;
struct Node
{
	char left;
	char right;
};
vector<Node>v;
void pre(char Node) {
	if (Node == '.')return;
	cout << Node;
	pre(v[Node].left);
	pre(v[Node].right);
}
void mid(char Node) {
	if (Node == '.')return;
	mid(v[Node].left);
	cout << Node;
	mid(v[Node].right);
}
void post(char Node) {
	if (Node == '.')return;
	//왼오루트
	post(v[Node].left);
	post(v[Node].right);
	cout << Node;
}
int main() {
	ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	cin >> n;
	v.resize(n);
	char root, l, r;
	for (int i = 0; i < n; i++) {
		cin >> root >> l >> r;
		v[root].left = l;
		v[root].right = r;
	}
	pre('A');
	cout << "\n";
	mid('A');
	cout << "\n";
	post('A');
	cout << "\n";	
}
