use proconio::input;

fn main() {
    input! {
        l1: u128,
        r1: u128,
        l2: u128,
        r2: u128,
    }
    let b1 = (1u128 << r1) - (1u128 << l1);
    let b2 = (1u128 << r2) - (1u128 << l2);
    let ans = b1 & b2;
    println!("{}", ans.count_ones());
}
