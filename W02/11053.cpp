#include <vector>
#include <algorithm>
#include <iostream>
#define FAST ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define MAX 1005
using namespace std;

int n;
int arr[MAX];

int main() {
    FAST;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int dp[MAX] = { 0 }; 
    dp[0] = 1;
    if (n == 1) {
        cout << 1;
        return 0;
    }
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) { 
            if (arr[i] > arr[j])
                dp[i] = max(dp[i], dp[j]);//핵심 아이디어
        }
        dp[i] += 1;
        //커밋 컨벤션 수정하기
    }
    cout << *max_element(dp, dp + n);
    return 0;
}
