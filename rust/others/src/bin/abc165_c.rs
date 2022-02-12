use itertools::Itertools;
use proconio::{marker::*, *};
fn main() {
    input! {
        (n,m,q):(usize,usize,usize),
        l:[(Usize1,Usize1,usize,u64);q]
    }
    let mut r = 0;
    for h in (0..m).combinations_with_replacement(n) {
        let mut s = 0;
        for &c in &l {
            if h[c.1] - h[c.0] == c.2 {
                s += c.3
            }
        }
        r = r.max(s);
    }
    print!("{}", r);
}
