fn main(){
    proconio::input!{
        a:isize,
        b:isize,
        c:isize
    }
    let d = gcd(gcd(a,b),c);
    println!("{}",a/d+b/d+c/d-3);
}
fn gcd(x:isize,y:isize)->isize{
    if y==0{x}else{gcd(y,x%y)}
}