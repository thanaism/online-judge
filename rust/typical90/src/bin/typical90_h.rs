use proconio::{input, marker::Chars};
fn main() {
    input!{ n:usize, s:Chars }
    let mut dp = vec![vec![0_i128; 8]; n+1];
    let atcoder = "atcoder ".chars().collect::<Vec<char>>();
    dp[0][0] = 1;
    const MOD: i128 = 1_000_000_007;
    for j in 0..8 {
        for i in 0..n {
            if s[i]==atcoder[j] {
                dp[i+1][j+1] += dp[i][j]%MOD;
            }
            dp[i+1][j] += dp[i][j]%MOD;
        }
    }
    println!("{}",dp[n][7]%MOD);
}