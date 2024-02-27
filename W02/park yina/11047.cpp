#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
#define MAX 11
#define FAST ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
typedef long long  ll;
ll k;
int arr[MAX];
int cnt;
int n;
int main() {
	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	for (int i = n-1; i >= 0; i--) {
			cnt += k / arr[i];
			k = k % arr[i];//몫을 나눈 나머지가 값이 된다.
	}
	cout << cnt;
	return 0;
}
//커밋 컨벤션 수정하기
