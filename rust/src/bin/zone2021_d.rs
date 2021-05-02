use proconio::{input,marker::Chars};
fn main(){
    input!{s:Chars}
    let mut t=std::collections::VecDeque::<char>::new();
    let mut r=false;
    for i in s{
        if i=='R'{r=!r}
        else{
            if r{
                if t.len()>0&&t.front()==Some(&i){t.pop_front();}
                else{t.push_front(i)}
            }else{
                if t.len()>0&&t.back()==Some(&i){t.pop_back();}
                else{t.push_back(i)}
            }
        }
    }
    let a:String=if r{t.iter().rev().collect()}else{t.iter().collect()};
    println!("{}",a);
}