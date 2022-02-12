use proconio::{input, marker::*};
fn main() {
    input!(c: Chars);
    println!(
        "{}",
        if c[0] == c[1] && c[0] == c[2] {
            "Won"
        } else {
            "Lost"
        }
    )
}
