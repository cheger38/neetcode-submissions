class Solution {
    public int climbStairs(int n) {
        int[] dp = new int[n];
        for (int i = 0; i < dp.length; i++) {
            dp[i] = -1;
        }

        dfs(n, 0, dp);

        return dp[0];
    }

    public int dfs(int n, int i, int[] dp) {
        if (i == n) return 1;
        if (i > n) return 0;
        if (dp[i] != -1) return dp[i];


        dp[i] = dfs(n, i + 1, dp) + dfs(n, i + 2, dp);
        return dp[i];
    }
}
