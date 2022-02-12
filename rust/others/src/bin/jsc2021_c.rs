fn main() {
    proconio::input!(a: i64, b: i64);
    let mut ans = 0;
    for i in 1..=200000 {
        if (a + i - 1) / i < b / i {
            ans = i;
        }
    }
    println!("{}", ans)
}
