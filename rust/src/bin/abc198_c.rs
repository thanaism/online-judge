use proconio::input;

fn main() {
    input! {
        r:i128,
        x:i128,
        y:i128
    }
    let dd:i128 = x * x + y * y;
    let rr:i128 = r * r;
    if dd < rr {
        println!("2");
    } else {
        let mut ok: i128 = 200000;
        let mut ng: i128 = 0;
        while (ok - ng).abs() > 1 {
            let mid:i128 = (ok + ng) / 2;
            if mid * mid * rr >= dd {
                ok = mid;
            } else {
                ng = mid;
            }
        }
        println!("{}", ok);
    }
}
