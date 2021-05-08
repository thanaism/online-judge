fn main() {
    proconio::input! {
        n: isize,
        a: [isize; n],
        b: [isize; n]
    }
    let mut u = 1001;
    let mut l = 0;
    for (i, j) in a.iter().zip(b.iter()) {
        if *i > l {
            l = *i
        }
        if *j < u {
            u = *j
        }
    }
    let c = u - l + 1;
    println!("{}", if c < 0 { 0 } else { c });
}
