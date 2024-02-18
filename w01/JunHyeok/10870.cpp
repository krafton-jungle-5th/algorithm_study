#include <iostream>

using namespace std;

int n;
int res = 0;

int func(int val) {
    if (val == 0) {
        return 0;
    }
    else if (val <= 2) {
        return 1;
    }
    else {
        return func(val-1) + func(val-2);
    }
}

int main () {
    cin >> n;

    res = func(n);
    cout << res;

    return 0;
}