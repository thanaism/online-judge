fn main() {
    proconio::input! {n:usize,a:[usize;n]}
    let mut x = 0;
    for l in 0..n {
        let mut y = a[l];
        for r in l..n {
            y = std::cmp::min(y, a[r]);
            x = std::cmp::max((r - l + 1) * y, x)
        }
    }
    println!("{}", x);
}
