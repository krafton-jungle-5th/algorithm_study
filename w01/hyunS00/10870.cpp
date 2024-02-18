#include<bits/stdc++.h>
using namespace std;

int main(){
    int N, tmp,fibo1 = 0, fibo2 = 1;
    cin >> N;
    for(int i=0; i< N-1 ; i++){
        tmp = fibo2;
        fibo2 = fibo1 + fibo2;
        fibo1 = tmp;
    }
    if(N>0) cout << fibo2 << endl;
    else cout << 0 << endl;
}