// 팰린드롬인지 확인하기
// https://www.acmicpc.net/problem/10988

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int sol() {
    string W;
    getline(cin, W); // 공백 포함 한 줄 읽기

    int f = 0;
    int r = W.length() - 1; // 문자열 길이

    while (f < r) {
        if (W[f] != W[r]) {
            return 0; // 팰린드롬이 아니면 0 반환
        }
        f++;
        r--;
    }
    return 1; // 팰린드롬이면 1 반환
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); // 입출력 속도 향상

    cout << sol() << endl;

    return 0;
}