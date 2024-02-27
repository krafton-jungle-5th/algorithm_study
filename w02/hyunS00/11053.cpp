#include<bits/stdc++.h>
using namespace std;

int main(){
    int N;
    int A[1001] = {0,};
    int dp[1001] = {0,};

    cin >> N;

    for(int i = 0; i < N; i++){
        int num;
        cin >> num;
        A[i+1] = num;
    }

    dp[1] = 1;
    for(int i = 2; i <= N; i++){
        int max = -1;
        for(int j = i; j > 0; j--){
            if(A[i] > A[j] && max < dp[j]){
                max = dp[j];
            }
        }
        if(max == -1) dp[i] = 1;
        else dp[i] = max + 1;
    }

    int max = -1;
    for(int i = 1; i <= N; i++){
        if(max < dp[i]) max = dp[i];
    }

    cout << max << "\n";
}