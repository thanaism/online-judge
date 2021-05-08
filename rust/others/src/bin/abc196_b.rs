fn main(){
    proconio::input!{s:String};
    println!("{}",s.split('.').nth(0).unwrap());
}
