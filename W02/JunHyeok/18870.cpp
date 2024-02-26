#include<iostream>
#include<map>
#include<algorithm>

using namespace std;

int n;
int arr[1000000];
int sortedArr[1000000];
map<int,int> mmap;

int main() {
    cin >> n;

    int rank = 0;

    for (int i=0; i<n; i++) {
        cin >> arr[i];
        sortedArr[i] = arr[i];
    }

    sort(sortedArr, sortedArr + n);

    for (int i=0; i<n; i++) {
        int val = sortedArr[i];

        if (mmap.find(val) == mmap.end()) { // Doesn't Exist
            mmap[val] = rank;
            rank++;
        }
    }

    for (int i=0; i<n; i++) {
        int tmp = arr[i];
        cout << mmap[tmp] << " ";
    }

    return 0;
}