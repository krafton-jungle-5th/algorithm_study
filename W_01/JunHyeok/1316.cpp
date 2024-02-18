#include <iostream>
#include <string>
#include <map>

using namespace std;

const int MAX_ROWS = 100; // 최대 행 수
const int MAX_COLS = 100; // 최대 열 수
    
int res;

int main() {
    string input[MAX_ROWS][MAX_COLS]; // 최대 크기의 2차원 배열 선언

    // 입력 받기
    int n;
    cin >> n;
    cin.ignore(); // 개행 문자 무시
    cout << "\n";
    for (int i = 0; i < n; ++i) {
        string line;
        getline(cin, line);
        bool flag = true;
        map<char,int> dict;

        for (int i=0; i< line.size(); i++) {
            char c = line[i];

            auto tmp = dict.find(c);
            if (tmp == dict.end()) {
                dict[c] = 1;
            } else {
                if (line[i] == line[i-1]) {
                    continue;
                }
                else {
                    flag = false;
                    break;
                }
            }
        }
        if (flag) res++;
    }
    cout << res;
    return 0;
}
