#include <iostream>

using namespace std;

int n;
int arr[100];
int res = 0;

int main() {

    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }

    for (int i=0; i<n; i++) {
        bool flag = true;
        int tmp = arr[i];

        if (tmp == 1 | tmp == 0) {
            continue;
        }
        else {
            for (int j=2; j<=tmp/2; j++) {
                if (tmp%j == 0) {
                    flag = false;
                    break;
                }
            }
        }
        if (flag) res++;
    }
    cout << res;

    return 0;
}
