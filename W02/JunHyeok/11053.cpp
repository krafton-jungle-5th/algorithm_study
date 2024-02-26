#include <iostream>

using namespace std;

// 1) 
int n;
int arr[1000001] = {0,};
int dp[1000001] = {1,};
int res = 0;

int main () {
    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }

    for (int i=0; i<n; ++i) {
        dp[i] = 1;
        for (int j=0; j<i; ++j) {
            if (arr[i] > arr[j]) {
                dp[i] = max(dp[i], dp[j]+1);
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        res = max(res, dp[i]);
    }
    cout<<res;

    return 0;
}
