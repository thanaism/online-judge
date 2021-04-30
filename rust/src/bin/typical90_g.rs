use proconio::input;
fn main(){
    input!{
        n:usize,
        mut a:[usize;n],
        q:usize,
        b:[usize;q]
    }
    a.sort();
    for i in b{
        let mut ans=0;
        let mut ok:usize=n-1;
        let mut ng:usize=0;
        while ok-ng>1{
            let mid = (ok+ng)/2;
            //println!("{}",mid);
            if is_ok(&a,mid,i){
                ok=mid;
            }else{
                ng=mid;
            }
        }
        if ok==0{
            ans+=((i-a[ok]) as isize).abs();
        }else if ((i-a[ok]) as isize).abs()<((i-a[ok-1]) as isize).abs(){
            ans+=((i-a[ok]) as isize).abs();
        }else{
            ans+=((i-a[ok-1]) as isize).abs();
        }
        println!("{}",ans);
    }
}

fn is_ok(a:&Vec<usize>,m:usize,i:usize)->bool{
    a[m]>=i
}