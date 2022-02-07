#include <bits/stdc++.h>
using namespace std;
using ll = long long;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    stack<int> stk;
    int ans = 0;

    for (int i = 0; i < n; ++i) {
        int a, b;
        cin >> a >> b;

        if (stk.empty() || stk.top() < b) 
            stk.push(b);
        else if (stk.top() != b) {
            while (!stk.empty() && stk.top() > b) {
                stk.pop();
                ans++;
            }

            if (stk.empty() || stk.top() < b)
                stk.push(b);
        }
    }
    
    while (!stk.empty()) {
        if (stk.top() != 0)
            ans++;
        stk.pop();
    }
    cout << ans << '\n';
}