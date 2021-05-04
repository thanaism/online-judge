fn main(){
    proconio::input!{n:usize,_:i32,mut s:[String;n]}
    s.sort();
    let a:String = s.iter().fold("".to_string(),|x,y|x+&y);
    println!("{}",a);
}