fn main() {
    proconio::input!{
        (n,k):(usize,usize),
        a:[usize;n]
    }
    let mut right = 0;
    let mut ans = 0;
    let mut cnt = 0;
    let mut dic = std::collections::HashMap::new();
    for left in 0..n {
        while right<n {
            if *dic.entry(a[right]).or_insert(0)==0 {
                if cnt==k { break }
                else { cnt+=1 }
            }
            *dic.entry(a[right]).or_insert(0) += 1;
            right += 1;
        }
        ans = ans.max(right-left);
        if *dic.entry(a[left]).or_insert(0)==1 { cnt -= 1 }
        *dic.entry(a[left]).or_insert(0) -= 1;
    }
    println!("{}",ans);
}