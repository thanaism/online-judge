use proconio::input;

fn main(){
    input!{
        n:usize,
        mut a:[usize;n],
        q:usize,
        b:[usize;q]
    };
    a.sort();
    for i in b{
        let mut ok = 0;
        let mut ng = n-1;
        while ((ok-ng) as isize).abs()>1 {
            let mid:usize=(ok+ng)/2;
            println!("mid: {}",mid);
            if a[mid]<i {
                ok=mid;
            }else{
                ng=mid;
            }
        }
        println!("{}",ok)
    }
}