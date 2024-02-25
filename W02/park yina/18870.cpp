#include<iostream>
#include<algorithm>
#include<vector>
#include<unordered_map>
using namespace std;
#define MAX 1000005
typedef long long ll;
ll n;
vector<ll>v;
vector <ll>v2;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	cin >> n;
	for (int i = 0; i < n; i++) {
		int num = 0;
		cin >> num;
		v.push_back(num);
		v2.push_back(num);
	}
	sort(v2.begin(), v2.end());
	v2.erase(unique(v2.begin(), v2.end()),v2.end());
	for (int i = 0; i < n; i++) {
		cout<<lower_bound(v2.begin(), v2.end(), v[i])-v2.begin()<<" ";
	}
	return 0;
}
