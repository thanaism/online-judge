fn main() {
    proconio::input! {n:i64,d:f64,h:f64,p:[(f64,f64);n]}
    let mut a = 0f64;
    for (i, j) in p {
        a = a.max(h - d * (h - j) / (d - i))
    }
    println!("{}", a);
}
