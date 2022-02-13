use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        n: usize,
        q: usize,
        a: [usize; n],
        xk: [(usize, usize); q],
    }
    let mut map = HashMap::new();
    let mut ans = HashMap::new();
    for i in 0..n {
        *map.entry(a[i]).or_insert(0usize) += 1usize;
        let key: (usize, usize) = (a[i], map[&a[i]]);
        ans.insert(key, i + 1);
    }
    for i in 0..q {
        let key = xk[i];
        if ans.contains_key(&key) {
            println!("{}", ans[&key]);
        } else {
            println!("-1");
        }
    }
}
