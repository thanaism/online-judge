fn main() {
    proconio::input!{
        n: usize,
        l: [(usize,usize,usize,usize); n]
    }
    let mut imos = vec![vec![0i32;1100];1100];
    for &(x1,y1,x2,y2) in &l {
        imos[x1][y1] += 1;
        imos[x2][y1] -= 1;
        imos[x2][y2] += 1;
        imos[x1][y2] -= 1;
    }
    for i in 0..1010 {
        for j in 0..1010 {
            imos[i+1][j] += imos[i][j];
        }
    }
    for i in 0..1010 {
        for j in 0..1010 {
            imos[i][j+1] += imos[i][j];
        }
    }
    let mut cnt = vec![0;n+1];
    for i in 0..1010 {
        for j in 0..1010 {
            let k = imos[i][j] as usize;
            cnt[k] += 1;
        }
    }
    for i in 1..=n {
        println!("{}",cnt[i]);
    }
}