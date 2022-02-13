use itertools::Itertools;
use proconio::{input, marker::Chars};
use std::collections::VecDeque;

fn main() {
    input! {
        n: usize,
        s: Chars,
    }
    let mut ql = VecDeque::new();
    let mut qr = VecDeque::new();
    for i in 0..n {
        if s[i] == 'L' {
            qr.push_front(i);
        } else {
            ql.push_back(i);
        }
    }
    let mut ans = VecDeque::new();
    ans.append(&mut ql);
    ans.push_back(n);
    ans.append(&mut qr);
    println!("{}", ans.iter().join(" "));
}
