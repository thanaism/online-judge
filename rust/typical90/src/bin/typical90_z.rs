use proconio::{input,marker::Usize1};
fn main() {
    input!{
        n:usize,
        l:[(Usize1,Usize1);n-1]
    }
    let mut connected = vec![vec![];n];
    for &(a,b) in &l {
        connected[a].push(b);
        connected[b].push(a);
    }
    let mut dist = vec![-1i32;n];
    bfs(&connected,&mut dist);
    let mut odd = Vec::new();
    let mut even = Vec::new();
    for i in 0..n {
        if dist[i]&1==1 { odd.push((i+1).to_string()) }
        else { even.push((i+1).to_string()) }
        let p = |x:Vec<String>|println!("{}",x.join(" "));
        if odd.len()==n/2 { p(odd); break; }
        if even.len()==n/2 { p(even); break; }
    }
}

fn bfs(connected: &Vec<Vec<usize>>, dist: &mut Vec<i32>) {
    let mut q = std::collections::VecDeque::new();
    q.push_back(0);
    dist[0] = 0;
    while q.len()>0 {
        let i = q.pop_front().unwrap();
        for &j in &connected[i] {
            if dist[j]==-1 {
                dist[j] = dist[i]+1;
                q.push_back(j);
            }
        }
    }
}