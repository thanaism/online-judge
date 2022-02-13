use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        n: usize,
        a: [usize; 4 * n - 1],
    }
    let mut counter = HashMap::new();
    for i in a {
        *counter.entry(i).or_insert(0usize) += 1;
    }
    for (key, value) in counter {
        if value % 4 != 0 {
            println!("{}", key);
        }
    }
}
