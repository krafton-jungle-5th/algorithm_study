#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, K, cnt = 0;
    vector <int> coins;

    cin >> N >> K;

    for(int i = 0; i < N; i++){
        int coin;
        cin >> coin;
        coins.push_back(coin);
    }

    for(int i = N - 1; i >= 0; i--){
        if(i <= K){
            cnt += K / coins[i];
            K %= coins[i];
        }

        if(K <= 0) break;
    }

    cout << cnt << "\n";
}