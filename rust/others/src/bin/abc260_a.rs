use proconio::input;

fn main() {
    input! { s: String }
    let mut ans = (-1).to_string();
    for c in s.chars() {
        let n = s.matches(c).count();
        if n == 1 {
            ans = c.to_string();
        }
    }
    println!("{}", ans);
}
