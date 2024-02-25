#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    int N;
    cin >> N;

    vector<int> nums;
    vector<int> uniqueNums;

    for(int i = 0; i < N; i++){
        int x;
        cin >> x;

        nums.push_back(x);
        uniqueNums.push_back(x);
    }

    sort(uniqueNums.begin(), uniqueNums.end());
    uniqueNums.erase(unique(uniqueNums.begin(),uniqueNums.end()),uniqueNums.end());

    for(int i : nums){
        int idx = lower_bound(uniqueNums.begin(), uniqueNums.end(), i) - uniqueNums.begin();
        cout << idx << " ";
    }
}