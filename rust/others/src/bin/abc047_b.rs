fn main(){
    proconio::input!{w:usize,h:usize,n:i32,p:[(usize,usize,i32);n]}
    let mut g=vec![vec![0;w];h];
    for k in p{
        let (x,y,a)=k;
        for i in 0..h{for j in 0..w{match a{
            1=>if j<x{g[i][j]=1},
            2=>if j>=x{g[i][j]=1},
            3=>if i<y{g[i][j]=1},
            4=>if i>=y{g[i][j]=1},
            _=>()
        }}}
    }
    println!("{}",w*h-g.iter().flatten().sum::<usize>());
}