fn main(){
    proconio::input!{
        (n,m,x):(usize,usize,i64),
        l:[(i64,[i64;m]);n]
    }
    let mut ans = 1<<30;
    for i in 0..1<<n {
        let mut cost = 0;
        let mut stat = vec![0;m];
        for j in 0..n {
            if i>>j&1==1{
                cost += l[j].0;
                for k in 0..m {
                    stat[k] += l[j].1[k];
                }
            }
        }
        let mut ok = true;
        for k in 0..m {
            if stat[k]<x {ok=false}
        }
        if ok {ans=ans.min(cost)}
    }
    println!("{}",if ans==1<<30 {-1} else {ans});
}