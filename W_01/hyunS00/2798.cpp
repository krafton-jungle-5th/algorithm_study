#include<bits/stdc++.h>
using namespace std;

int main(){
    int N, M,sum,maxNum=0;
    cin >> N >> M;
    int cardNums[N];

    for(int i=0;i<N;i++){
        cin >> cardNums[i];
    }

    for(int i=0;i<N-2;i++){
        for(int j=i+1; j<N-1 ;j++){
            for(int k=j+1;k<N;k++){
                sum = cardNums[i]+cardNums[j]+cardNums[k];
                if(sum <= M){
                    maxNum = max(maxNum,sum);
                }
            }
        }
    }

    cout << maxNum << "\n";
}