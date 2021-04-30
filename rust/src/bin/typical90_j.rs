fn main(){
    proconio::input!{
        n:usize,
        cp:[(usize,usize);n],
        q:usize,
        lr:[(usize,usize);q]
    }
    let mut one:Vec<usize>=(0..=n).map(|_|0).collect();
    let mut two:Vec<usize>=(0..=n).map(|_|0).collect();
    for i in 0..n{
        if cp[i].0==1{
            one[i+1]=cp[i].1+one[i];
            two[i+1]=two[i];
        }else{
            one[i+1]=one[i];
            two[i+1]=cp[i].1+two[i];
        }
    }
    for i in 0..q{
        let (l,r)=lr[i];
        println!("{} {}",one[r]-one[l-1],two[r]-two[l-1]);
    }
}