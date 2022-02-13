use proconio::{input, marker::Chars};

fn main() {
    input! {
        mut s: Chars,
    }
    let mut tail = 0;
    for i in (0..s.len()).rev() {
        if s[i] != 'a' {
            break;
        }
        tail += 1;
    }
    let mut front = 0;
    for i in 0..s.len() {
        if s[i] != 'a' {
            break;
        }
        front += 1;
    }
    if front > tail {
        println!("No");
    } else {
        let mut t = vec!['a'; tail - front];
        t.append(&mut s);
        let n = t.len();
        let mut ok = true;
        for i in 0..n {
            if t[i] != t[n - i - 1] {
                ok = false;
            }
        }
        println!("{}", if ok { "Yes" } else { "No" });
    }
}
