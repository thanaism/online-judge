fn main() {
    proconio::input! {
        n:usize,
        mut a:[i64;n],
        mut b:[i64;n],
    }
    a.sort();
    b.sort();
    let ans: i64 = (0..n)
        .map(|i| (a[i] - b[i]).abs())
        .collect::<Vec<_>>()
        .iter()
        .sum();
    println!("{}", ans);
}
