fn main() {
    proconio::input! {w:f64,h:f64,x:f64,y:f64}
    print!(
        "{} {}",
        w * h / 2.0,
        if 2.0 * x == w && 2.0 * y == h { 1 } else { 0 }
    )
}
