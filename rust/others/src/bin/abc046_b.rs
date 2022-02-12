fn main() {
    proconio::input! {n:u32,k:i64}
    println!("{}", k * (!-k).pow(n - 1))
}
