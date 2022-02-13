use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        n: usize,
        m: usize,
        s: [String; n],
        t: [String; m],
    }
    let mut hs = HashSet::new();
    for i in 0..m {
        hs.insert(t[i].to_owned());
    }
    for i in 0..n {
        if hs.contains(&s[i]) {
            println!("Yes");
        } else {
            println!("No");
        }
    }
}
