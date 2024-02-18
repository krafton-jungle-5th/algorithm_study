#include<bits/stdc++.h>
using namespace std;

int main(){
    vector<pair<int,int>> bodys;
   
    int N,x,y;
    cin >> N;
    vector<int>tmp;

    for(int i=0; i<N ; i++){
        cin >> x >> y;
        pair<int,int> body;
        body.first = x;
        body.second = y;
        bodys.push_back(body);
        tmp.push_back(1);
    }

    for(int i=0; i<N; i++){
        for(int j=i+1; j<N; j++){
            if(bodys[i].first < bodys[j].first && bodys[i].second < bodys[j].second){
                tmp[i]++;
            }else if(bodys[i].first > bodys[j].first && bodys[i].second > bodys[j].second){
                tmp[j]++;
            }
        }
    }
    for(int i=0; i<N;i++){
        cout << tmp[i] << endl;
    }
}