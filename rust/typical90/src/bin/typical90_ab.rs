fn main() {
    proconio::input!{
        n: usize,
        l: [(usize,usize,usize,usize); n]
    }
    let mut imos = vec![vec![0i32;1002];1002];
    for &(x1,y1,x2,y2) in &l {
        imos[x1][y1] += 1;
        imos[x2][y1] -= 1;
        imos[x2][y2] += 1;
        imos[x1][y2] -= 1;
    }
    let mut acc = vec![vec![0i32;1003];1003];
    for i in 0..1002 {
        for j in 0..1002 {
            acc[i+1][j] += acc[i][j]+imos[i][j];
        }
    }
    let mut cnt = vec![0;n+1];
    for i in 0..1002 {
        for j in 0..1002 {
            acc[i][j+1] += acc[i][j];
            let k = acc[i][j+1] as usize;
            cnt[k] += 1;
        }
    }
    for i in 1..=n {
        println!("{}",cnt[i]);
    }
}