#include <bits/stdc++.h>
using namespace std;

void progression(int count, int N, int M);

vector <int> nums(9,0);
vector <int> useNum(9,0);

int main(){
    int N,M;

    cin >> N >> M;

    progression(0,N,M);
}

void progression(int count, int N, int M){
    if(count >= M ){
        for(int i = 0; i < M; i++){
            cout << nums[i] << " ";
        }
        cout << "\n";
        return;
    }
    for(int i = 1; i <= N; i++){
        if(useNum[i] == 0){
            useNum[i] = 1;
            nums[count] = i;
            progression(count+1,N,M);
            useNum[i] = 0;
        }
    }
}