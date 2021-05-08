use proconio::{input,marker::*};

fn main(){
    input!{
        h:usize,
        w:usize,
        x:Usize1,
        y:Usize1,
        s:[Chars;h],
    }
    let mut ans=1;
    for i in (0..x).rev(){
        if s[i][y]=='.'{ans+=1}else{break}
    }
    for i in (x+1)..h{
        if s[i][y]=='.'{ans+=1}else{break}
    }
    for i in (0..y).rev(){
        if s[x][i]=='.'{ans+=1}else{break}
    }
    for i in (y+1)..w{
        if s[x][i]=='.'{ans+=1}else{break}
    }
    println!("{}",ans);
}