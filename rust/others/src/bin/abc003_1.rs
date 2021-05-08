fn main(){
    proconio::input!{n:isize}
    let mut a:isize = 0;
    for i in 1..(n+1){a+=i}
    let b:f32=10000_f32*(a as f32)/(n as f32);
    println!("{}",b)
}