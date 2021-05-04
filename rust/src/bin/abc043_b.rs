fn main(){
    proconio::input!{s:String}
    let mut t = format!{""};
    for c in s.chars(){
        if c=='0'{t.push(c)}  
        if c=='1'{t.push(c)}  
        if c=='B'{t.pop();}  
    }
    println!("{}",t);
}