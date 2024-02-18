#include<iostream>
using namespace std;
int solve(int n) {
	if (n == 0||n==1)return n;
	else return (solve(n - 1) + solve(n - 2));
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int input = 0;
	cin >> input;
	cout<<solve(input);
}
//최적화 이후 코드(메모제이션 기법 활용 코드)
#include<iostream>
#include<vector>
using namespace std;

vector<int> memo;

int solve(int n) {
    if (memo[n] != -1) 
        return memo[n];
    
    if (n == 0 || n == 1)
        return n;
    else {
        memo[n] = solve(n - 1) + solve(n - 2);
        return memo[n];
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    int input = 0;
    cin >> input;
    
    memo.assign(input + 1, -1); // 메모 배열 초기화
    cout << solve(input);
    
    return 0;
}
