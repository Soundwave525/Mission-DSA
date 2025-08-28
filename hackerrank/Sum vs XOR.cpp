#include <bits/stdc++.h>
using namespace std;

long sumXor(long n) {
    if (n == 0) return 1;

    long zeroBits = 0;
    long t = n;

    while (t > 0) {
        if ((t & 1) == 0) {  
            zeroBits++;
        }
        t >>= 1;
    }

    return 1L << zeroBits;
}

int main() {
    long n;
    cin >> n;

    cout << sumXor(n) << endl;
    return 0;
}
