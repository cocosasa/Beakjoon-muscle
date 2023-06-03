#include<iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int tc;
    int T;
    cin >> T;
    for (tc = 1; tc <= T; ++tc)
    {
        int N;
        int check = 0;
        int CN = 0;

        cin >> N;

        while (true) {
            CN += N;

            int tmp = CN;

            while (tmp > 0) {
                check |= 1 << (tmp % 10);
                tmp /= 10;
            }

            if (check == (1 << 10) - 1) break;
        }

        cout << '#' << tc << ' ' << CN << endl;
    }
    return 0;
}