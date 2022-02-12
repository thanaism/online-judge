fn main() {
    proconio::input! {a:i64,b:i64,c:i64,d:i64}
    let f = |x| b / x - (a + x - 1) / x + 1;
    println!("{}", b - a + 1 - f(c) - f(d) + f(c * d / g(c, d)));
}
fn g(x: i64, y: i64) -> i64 {
    if y == 0 {
        x
    } else {
        g(y, x % y)
    }
}
