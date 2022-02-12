use itertools::iproduct;
use proconio::{input, marker::Chars};
fn main() {
    input! {
        h:usize, w:usize, k:usize,
        c:[Chars;h]
    }
    let f = |x, y| x >> y & 1 == 1;
    let ans = iproduct!(0..1 << h, 0..1 << w)
        .filter(|&(i, j)| {
            k == iproduct!(0..h, 0..w)
                .filter(|&(p, q)| c[p][q] == '#' && f(i, p) && f(j, q))
                .count()
        })
        .count();
    println!("{}", ans);
}
