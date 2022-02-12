use proconio::input;
use std::cmp::min;

fn main() {
    input! {
        H: usize,
        W: usize,
        K: usize,
        A: [[usize; W]; H],
    }
    let INF: usize = 1 << 60;
    let mut dp = vec![vec![vec![INF; K + 1]; W]; H];
    let mut ans = INF;
    for X in 0..H {
        for Y in 0..W {
            let x = A[X][Y];
            for i in 0..H {
                for j in 0..W {
                    for k in 0..=K {
                        dp[i][j][k] = INF;
                    }
                }
            }
            if A[0][0] >= x {
                dp[0][0][1] = A[0][0];
            }
            if A[0][0] <= x {
                dp[0][0][0] = 0;
            }
            for i in 0..H {
                for j in 0..W {
                    for k in 0..=K {
                        if i > 0 {
                            if k < K && A[i][j] >= x {
                                dp[i][j][k + 1] = min(dp[i][j][k + 1], dp[i - 1][j][k] + A[i][j]);
                            }
                            if A[i][j] <= x {
                                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k]);
                            }
                        }
                        if j > 0 {
                            if k < K && A[i][j] >= x {
                                dp[i][j][k + 1] = min(dp[i][j][k + 1], dp[i][j - 1][k] + A[i][j]);
                            }
                            if A[i][j] <= x {
                                dp[i][j][k] = min(dp[i][j][k], dp[i][j - 1][k]);
                            }
                        }
                    }
                }
            }
            ans = min(ans, dp[H - 1][W - 1][K]);
        }
    }
    println!("{}", ans);
}
