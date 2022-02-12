fn main() {
    proconio::input! {
        (a,b):(i128,f64)
    }
    println!("{}", (b * 100.001) as i128 * a / 100);
}
