fn main() {
    proconio::input!(n: u32, m: u32, a: [u32; n], b: [u32; m]);
    for i in 1..=1000 {
        if a.contains(&i) ^ b.contains(&i) {
            print!("{} ", i);
        }
    }
}
