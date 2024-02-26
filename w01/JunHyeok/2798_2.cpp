#include <iostream>
#include <vector>

using namespace std;

int n, target;
int arr[100] = {0,};
int res = 0;
int sum = 0;
vector<int> vect;

void func(int start, int idx) {
    if (idx == 3) {
        for (auto i : vect) {
//            cout << i << " "; 각 단계별로 어떤 조합을 사용하는지 보고싶으면 주석을 해제하세요
            sum += i;
        }
//        cout << "Sum : " << sum << "\n"; 각 단계별로 어떤 조합을 사용하는지 보고싶으면 주석을 해제하세요
        if (sum <= target) {
            res = max(res,sum);
        }
        sum = 0;
        return;
    }

    for (int i=start; i<n; i++) {
        vect.push_back(arr[i]);
        func(i + 1, idx + 1);
        vect.pop_back();
    }
}

int main() {

    cin >> n >> target;

    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }

    func(0,0);

    cout << res;
    return 0;
}
