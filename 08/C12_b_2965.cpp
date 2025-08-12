// 캥거루 세마리
// https://www.acmicpc.net/problem/2965

#include <iostream>
#include <algorithm>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int A, B, C;
    std::cin >> A >> B >> C;

    int gap1 = B - A - 1;
    int gap2 = C - B - 1;

    std::cout << std::max(gap1, gap2) << std::endl;

    return 0;
}