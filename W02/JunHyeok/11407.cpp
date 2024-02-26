#include<iostream>

using namespace std;

int n, target;
int arr[1000000] = {0,};
int res = 0;

int main() {
    cin >> n >> target;
    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }

    //sort(arr, arr+n); 이미 정렬이 되어있네.
    reverse(arr,arr+n);

    for (int i=0; i<n; i++) {
        if ((target / arr[i]) > 0)  {
            res += target/arr[i];
            target = target%arr[i];
        }
    }
    cout << res;

    return 0;
}
