#include <bits/stdc++.h>
using namespace std;
using ll = long long;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n; cin >> n;
    
    deque<int> dq;
    for (int i = n; i > 0; --i) 
        dq.push_back(i);
    
    int ans[1000001];
    for (int i = n; i > 0; --i) {
        int t; cin >> t;

        if (t == 1) {
            ans[dq.back()] = i;
            dq.pop_back();
        }
        else if (t == 2) {
            int a = dq.back();
            dq.pop_back();
            ans[dq.back()] = i;
            dq.pop_back();
            dq.push_back(a);
        }
        else if (t == 3) {
            ans[dq.front()] = i;
            dq.pop_front();
        }
    }

    for (int i = 1; i <= n; ++i)
        cout << ans[i] << ' ';
    cout << '\n';
}