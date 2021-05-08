fn main(){
    proconio::input!{l:usize,r:usize}
    let mut u = 2019;
    let r=r.min(l+2019);
    for i in l..r {
        for j in i+1..=r {
            u=u.min(i*j%2019)
        }
    }
    println!("{}",u);
}