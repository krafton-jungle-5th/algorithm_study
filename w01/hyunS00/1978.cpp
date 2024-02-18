#include<bits/stdc++.h>
using namespace std;

int main(){
    int N,num,count=0;
    cin >> N;
    while(N>0){
        N--;
        cin >> num;
        int sum = 0;
        for(int i=2;i<=num;i++){
            if(num % i ==0) sum += i;
        }
        if(sum == num) count++;
    }
    cout << count << endl;
}