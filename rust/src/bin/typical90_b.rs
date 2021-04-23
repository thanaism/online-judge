fn main() {
    proconio::input!{
        n:isize
    }
    for i in 0..1<<n {
        let mut r=0;
        let mut l=0;
        let mut f=true;
        let mut s="".to_string();
        for j in 0..n {
            if i>>(n-j-1)&1 == 1{
                r+=1;
                s+=")";
            }else{
                l+=1;
                s+="(";
            }
            if r>l {f=false}
        }
        if r==l && f {
            println!("{}",s);
        }
    }
}