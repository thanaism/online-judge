fn main(){
    proconio::input!{n:i64}
    let mut a=0;
    for i in 1..=1000000{if n>=format!("{}{}",i,i).parse::<i64>().unwrap(){a+=1}}
    println!("{}",a)
}