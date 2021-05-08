fn main(){
    proconio::input!{
        n:usize, k:isize,
        a:[isize;n],
        b:[isize;n]
    }
    let mut d=0;
    for i in 0..n{
        d+=(a[i]-b[i]).abs();
    }
    println!("{}",if d<=k && (k-d)%2==0{"Yes"}else{"No"});
}