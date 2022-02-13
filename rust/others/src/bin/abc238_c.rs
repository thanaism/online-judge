use proconio::input;

fn main() {
    input! {
        n: usize,
    }
    let m = n.to_string().len();
    let mut ans = 0usize;
    const MOD: usize = 998244353;
    for i in 0..m {
        let x = 10usize.pow(i as u32);
        let y = std::cmp::min(x * 9, n - x + 1);
        let mut z = (y + 1) % MOD;
        z *= y % MOD;
        z %= MOD;
        z *= {
            let mut res = 1;
            let mut a = 2;
            let mut n = MOD - 2;
            while n > 0 {
                if n & 1 == 1 {
                    res = res * a % MOD
                }
                a = a * a % MOD;
                n >>= 1;
            }
            res
        };
        ans += z;
        ans %= MOD;
    }
    println!("{}", ans);
}
