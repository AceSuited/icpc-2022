#include <iostream>
using namespace std;

int a[1001];
int dp[1001];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    for (int i = 0; i < n; ++i)
        cin >> a[i];

    int ans = 0;
    for (int i = 0; i < n; ++i) {
        dp[a[i]] = a[i];
        int m = 0;
        for (int j = 0; j < a[i]; ++j)
            m = max(m, dp[j]);
        dp[a[i]] += m;
        ans = max(ans, dp[a[i]]);
    }

    cout << ans << '\n';
}
