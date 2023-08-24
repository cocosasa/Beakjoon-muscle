#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool isHanSu(const int a) {
    if (a < 100)
        return true;
    int a1, a2, a3;
    a3 = a / 100;
    a1 = a % 10;
    a2 = a % 100 / 10;
    if (a3 - a2 == a2 - a1)
        return true;
    return false;
}

int main() {
    int num, count = 0;
    cin >> num;

    for (int i = 1; i <= num; i++) {
        if (isHanSu(i)) {
            count++;
        }
    }
    cout << count;
}
