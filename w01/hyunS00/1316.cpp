#include<bits/stdc++.h>
using namespace std;

bool isGroupWord(int alpabet[], string word){
    int alpaIdx;
    for(int i=0; i<word.length();i++){
        alpaIdx = word[i]-'a';
        if(alpabet[alpaIdx] > -1 && i - alpabet[alpaIdx] > 1){
            return 0;
        }
        alpabet[alpaIdx] = i;
    }
    return 1;
}

int main(){
    int N;
    cin >> N;

    int alpabet[26];
    int cnt = 0;
    string word;


    while(N--){
        cin >> word;
        memset(alpabet,-1,sizeof(alpabet));
        if(isGroupWord(alpabet,word)) cnt++;
        
    }
    cout << cnt << endl;
}