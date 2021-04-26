fn main(){
    proconio::input!{
        h:usize,
        w:usize,
        a:[[usize;w];h]
    }
    let mut r:Vec<usize>=(0..h).map(|_|0).collect();
    let mut c:Vec<usize>=(0..w).map(|_|0).collect();
    for i in 0..h{
        for j in 0..w{
            r[i]+=a[i][j];
            c[j]+=a[i][j];
        }
    }
    for i in 0..h{
        let mut l:Vec<usize>=vec![];
        for j in 0..w{
            l.push(r[i]+c[j]-a[i][j]);
        }
        println!("{:?}",l);
    }

}