use proconio::{input,marker::Usize1};
use std::collections::VecDeque;
fn main(){
    input!{n:usize}
    let mut g:Vec<Vec<usize>>=(0..n).map(|_|vec![]).collect();
    for _ in 1..n{
        input!{x:Usize1,y:Usize1}
        g[x].push(y);
        g[y].push(x);
    }
    let mut q:VecDeque<usize>=VecDeque::new();
    let mut v:Vec<usize>=(0..n).map(|_|0).collect();
    let mut d:usize;
    v[0]=1;
    q.push_back(0);
    while q.len()>0{
        let i=q.pop_front().unwrap();
        d=v[i];
        for j in g[i].iter(){
            if v[*j]==0{
                q.push_back(*j);
                v[*j]=d+1;
            }
        }
    }
    let mut u:usize=0;
    for i in 0..n{
        if i==*v.iter().max().unwrap(){u=i}
    }
    v=(0..n).map(|_|0).collect();
    v[u]=1;
    q.push_back(u);
    while q.len()>0{
        let i=q.pop_front().unwrap();
        d=v[i];
        for j in g[i].iter(){
            if v[*j]==0{
                q.push_back(*j);
                v[*j]=d+1;
            }
        }
    }
    println!("{}",v.iter().max().unwrap());
}