fn main(){
    proconio::input!{n:i64,d:f64,h:f64,p:[(f64,f64);n]}
    let mut a=0f64;
    for(i,j)in p{let b:f64=h-d*(h-j)/(d-i);if b>a{a=b}}
    println!("{}",a);
}