// 크냐?
// https://www.acmicpc.net/problem/4101

#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int a, b;
    
    while (true) {
        cin >> a >> b;
        
        if (!a && !b) {
            break;
        }
        
        if (a > b) {
            cout << "Yes\n";
        } 
        else {
            cout << "No\n";
        }
    }
}