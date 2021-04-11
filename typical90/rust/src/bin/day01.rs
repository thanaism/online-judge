use proconio::input;

fn main() {
    input! {
        n: isize,
        l: isize,
        k: isize,
        a: [isize; n]
    }

    let mut ok: isize = 1;
    let mut ng: isize = l + 1;
    while (ng - ok).abs() > 1 {
        let mid = (ng + ok) / 2;
        let mut pre = 0;
        let mut cnt = 0;
        for i in &a {
            if i - pre >= mid && l - i >= mid {
                pre = *i;
                cnt += 1;
            }
        }
        if cnt >= k {
            ok = mid;
        } else {
            ng = mid;
        }
    }
    println!("{}", ok);
}
