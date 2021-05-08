fn main(){
    proconio::input!{
        (n,m,k):(usize,usize,usize),
        a:[usize;n],
        b:[usize;m]
    }
    let mut ca = vec![0];
    let mut cb = vec![0];
    for i in 0..n {ca.push(ca[i]+a[i])}
    for i in 0..m {cb.push(cb[i]+b[i])}
    let mut right = m;
    let mut ans = 0;
    for left in 0..=n {
        if ca[left] > k { break }
        while cb[right] > k-ca[left] {
            right -= 1;
        }
        ans = ans.max(left+right);
    }
    println!("{}",ans);
}