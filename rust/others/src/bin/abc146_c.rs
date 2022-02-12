fn main() {
    proconio::input! {a:i64,b:i64,x:i64}
    let f = |n: i64| a * n + b * (n.to_string().len() as i64) <= x;
    let mut o = -1i64;
    let mut n = (x + 1).min(1000000001);
    while n - o > 1 {
        let m = (n + o) / 2;
        if f(m) {
            o = m
        } else {
            n = m
        }
    }
    println!("{}", if o != -1 { o } else { 0 });
}
