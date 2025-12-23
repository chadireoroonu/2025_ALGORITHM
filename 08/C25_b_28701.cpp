// 세제곱의 합
// https://www.acmicpc.net/problem/28701

#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    int N;
    cin >> N;

    long long a = 0;
    long long b = 0;
    
    for (int i = 1; i <= N; i++) {
        a += i;
        b += (long long)i * i * i;
    }

    cout << a << "\n";
    cout << a * a << "\n";
    cout << b << "\n";
}