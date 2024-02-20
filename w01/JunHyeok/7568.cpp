#include <iostream>

using namespace std;

int n;
int arr[50][2];
int res[50] = {0};

int main() {
    cin >> n;

    for (int i=0; i<n; i++) {
        cin >> arr[i][0] >> arr[i][1];
    }

    for (int i=0; i<n; i++) {
        int rank = 1;
        for (int j=0; j<n; j++) {
            if (arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1]) {
                rank++;
            }
        }
        cout << rank << " ";
    }

    return 0;
}