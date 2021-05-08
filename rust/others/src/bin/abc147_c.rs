use proconio::*;
fn main() {
    input! { n:usize }
    let mut a = vec![0;n];
    let mut x = vec![vec![0;n];n];
    let mut y = vec![vec![0;n];n];
    for i in 0..n {
        input! { ua:usize }
        a[i] = ua;
        for j in 0..ua {
            input! { ux:usize, uy:usize }
            x[i][j] = ux-1;
            y[i][j] = uy;
        }
    }
    let mut ans = 0;
    for b in 0..1<<n {
        let mut flg = true;
        for i in 0..n {
            if b>>i&1==0 { continue }
            for j in 0..a[i] {
                if (b>>x[i][j]&1)^y[i][j]==1 { flg = false }
            }
        }
        if flg {ans=ans.max(b.count_ones())}
    }
    println!("{}",ans);
}
