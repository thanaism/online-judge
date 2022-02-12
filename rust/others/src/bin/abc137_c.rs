use proconio::{marker::*, *};
fn main() {
    input! {n:usize,s:[Bytes;n]}
    let mut a = 0u64;
    let mut d = std::collections::HashMap::new();
    for mut s in s {
        s.sort();
        let k = d.entry(s).or_insert(0);
        a += *k;
        *k += 1;
    }
    println!("{}", a);
}
