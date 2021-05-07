fn main(){
    proconio::input!{mut n:i64}
    let mut s=format!("");
    while n>0{
        n-=1;
        s.insert(
            0,
            ((n%26)as u8+b'a')as char
        );
        n/=26;
    }
    println!("{}",s);
}