fn main() {
    const MOD: u64 = 1_000_000_007;
    proconio::input! {
        n:usize, m:usize,
        a:[usize;m]
    }
    let mut f = vec![true; n + 1];
    for i in a {
        f[i] = false
    }
    let mut d = vec![0; n + 1];
    d[0] = 1;
    for i in 0..n {
        d[i] %= MOD;
        if i < n && f[i + 1] {
            d[i + 1] += d[i]
        }
        if i < n - 1 && f[i + 2] {
            d[i + 2] += d[i]
        }
    }
    println!("{}", d[n] % MOD);
}
