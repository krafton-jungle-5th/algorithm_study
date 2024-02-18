#include <iostream>

using namespace std;

int n, target;
int arr[100] = {0,};
int res = 0;

int main() {

    cin >> n >> target;

    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }

    for (int i=0; i<n; i++) {
        for (int j=i+1; j<n; j++) {
            for (int z=j+1; z<n; z++) {
                int tmp = arr[i]+arr[j]+arr[z];
                if (tmp <= target) {
                    res = max(tmp,res);
                }
            }
        }
    }

    cout << res;
    return 0;
}