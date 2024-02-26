#include <iostream>
#include <vector>


using namespace std;

int n,m;
int arr[8];
vector<int> vect;
bool visited[8] = {false};

void dfs(int idx) {

    if (idx == m) {
        for (auto i : vect) {
            cout << i << " ";
        }
        cout << "\n";
    }

    for (int i=0; i<n; i++) {
        if (!visited[i]) {
            visited[i] = true;
            vect.push_back(arr[i]);
            dfs(idx+1);
            vect.pop_back();
            visited[i] = false;
        }
    }
}

int main() {
    cin >> n >> m;

    for (int i=0; i<n; i++) {
        arr[i] = i+1;
    }
    
    dfs(0);
    return 0;
}