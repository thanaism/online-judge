fn main() {
    proconio::input! {(mut a,mut b):(i32,i32)}
    let mut ans = Vec::new();
    let mut s = 1;
    if a < b {
        std::mem::swap(&mut a, &mut b);
        s = -1;
    }
    (1..=a).for_each(|i| ans.push((i * s).to_string()));
    (1..b).for_each(|i| ans.push((-i * s).to_string()));
    ans.push((-s * (b..=a).sum::<i32>()).to_string());
    println!("{}", ans.join(" "));
}
