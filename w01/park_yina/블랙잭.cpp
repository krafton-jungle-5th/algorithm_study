#include<iostream>
#include<algorithm>
#define MAX 105
#define FAST ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

int n, m;
int arr[MAX];

int main() {
    FAST;
    cin >> n >> m;
    int ans = -1; 
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + n);
    for (int i = 0; i < n - 2; i++) {
        for (int j = i + 1; j < n - 1; j++) {
            for (int k = j + 1; k < n; k++) {
                int sum = arr[i] + arr[j] + arr[k];
                if (sum <= m) {
                    ans = max(ans, sum); // 합이 m 이하인 경우에만 ans를 갱신
                }
            }
        }
    }
    cout << ans;
    return 0;
}
