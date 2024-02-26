#include <iostream>

using namespace std;

int n;
int board[128][128];
int white = 0;
int blue = 0;

void func(int y, int x, int div) {
    int color = board[y][x];
    bool flag = false;

    for (int row = y; row < y + div; row++) {
        for (int col = x; col < x + div; col++) {
            if (color != board[row][col]) {
                flag = true;
                break;
            }
        }
    }

    if (flag) {
        div = div/2;
        func(y,x,div);
        func(y+div,x,div);
        func(y,x+div,div);
        func(y+div,x+div,div);
    } else {
        color == 0 ? white++ : blue++;
    }

}

int main() {
    cin >> n;
    for (int y=0; y<n; y++) {
        for (int x=0; x<n; x++) {
            cin >> board[y][x];
        }
    }

    func(0,0,n);
    cout << white << "\n";
    cout << blue;
    return 0;
}