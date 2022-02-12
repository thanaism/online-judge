use proconio::input;
// use proconio::marker::Chars;

fn main() {
    input! {
        // s: Chars,
        s: String,
    }
    println!("{}{}", &s[1..], &s[..1])
    // println!("{}{}{}", s[1], s[2], s[0])
}
