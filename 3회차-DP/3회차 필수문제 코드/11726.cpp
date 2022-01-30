#include <bits/stdc++.h>
using namespace std;

int dp[1001];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;

    dp[0] = dp[1] = 1;
    for (int i = 2; i <= n; ++i)
        dp[i] = (dp[i-1] + dp[i-2]) % 10007;;

    cout << dp[n] << '\n';
}