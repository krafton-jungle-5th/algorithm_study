#include<bits/stdc++.h>
using namespace std;

int main(){
    int N;
    queue<int> deck;
    cin >> N;

    for(int i=1;i<=N;i++){
        deck.push(i);
    }
    
    while (deck.size()>1)
    {
        deck.pop();
        if(deck.size()<1) break;
        deck.push(deck.front());
        deck.pop();
    }
    
    cout << deck.front() << endl;
}