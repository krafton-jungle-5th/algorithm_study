#include<iostream>
#include<set>
#include<string>
#include<algorithm>
using namespace std;
#define FAST ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
int n;
int cnt;
int main() {
	FAST;
	cin >> n;
	for (int i = 0; i < n; i++) {
		string str;
		cin >> str;
		string str2;
		str2 = str;
		auto last = unique(str.begin(), str.end());
		str.erase(last, str.end());
		set<char>s(str2.begin(), str2.end());
		if (s.size() == str.length()) {
			cnt++;
		}
	}
	cout << cnt;
	return 0;
}
