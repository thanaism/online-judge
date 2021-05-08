use itertools::Itertools;
use proconio::{marker::*, *};
fn main() {
    input! {
        n:usize,
        a:[[i32;n];n],
        m:usize,
        l:[(Usize1,Usize1);m]
    }
    let mut ng = vec![vec![false; n]; n];
    for i in 0..m {
        let (x, y) = l[i];
        ng[x][y] = true;
        ng[y][x] = true;
    }
    let mut ans = 1 << 30;
    for i in (0..n).permutations(n) {
        let mut t = 0;
        let mut ok = true;
        for (j, &k) in i.iter().enumerate() {
            if j < n - 1 {
                let (x, y) = (i[j], i[j + 1]);
                if ng[x][y] {
                    ok = false
                }
            }
            t += a[k][j];
        }
        if ok {
            ans = ans.min(t)
        };
    }
    println!("{}", if ans == 1 << 30 { -1 } else { ans });
}
