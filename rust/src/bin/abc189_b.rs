fn main(){
    proconio::input!{n:usize,x:i64,l:[(i64,i64);n]}
    let mut t = 0;
    for i in 0..n{t+=l[i].0*l[i].1;if t>100*x{println!("{}",i+1);return}}
    println!("{}",-1);
}