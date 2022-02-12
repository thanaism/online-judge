fn main() {
    proconio::input! {a:isize,b:isize,c:isize};
    println!("{}", if a * a + b * b < c * c { "Yes" } else { "No" })
}
