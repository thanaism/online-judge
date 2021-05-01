fn main(){
    proconio::input!{
        n:usize,
        s:[String;n]
    }
    let mut d = std::collections::HashSet::new();
    for i in 0..n{
        if !d.contains(&s[i]){ println!("{}",i+1) }
        d.insert(&s[i]);
    }
}