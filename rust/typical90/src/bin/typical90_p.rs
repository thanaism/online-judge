fn main(){
    proconio::input!{
        n:usize,
        a:usize,
        b:usize,
        c:usize
    }
    // let mut ans = 1000000000;
    let mut ans = 1<<30;
    for i in 0..10000{
        for j in 0..10000{
            let d = n-a*i-b*j;
            if d%c==0{
                ans=std::cmp::min(ans,i+j+d/c);
            }
        }
    }
    println!("{}",ans);
}