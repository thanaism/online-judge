fn main(){
    proconio::input!{y:[String;3]}
    let mut x=y.iter().map(|z|z.chars()).collect::<Vec<_>>();
    let mut i=0usize;
    let mut s="";
    loop{ 
        match x[i].next(){
            Some('a')=>{s="A";i=0},
            Some('b')=>{s="B";i=1},
            Some('c')=>{s="C";i=2},
            _=>{println!("{}",s);break}
        }
    }
}