use proconio::{input,marker::{Chars,Usize1}};
fn main(){
	input!{n:usize,mut s:Chars,q:usize}
	let mut r=false;
	for _ in 0..q{
		input!{t:usize,mut a:Usize1,mut b:Usize1}
		if r{a=(a+n)%(n+n);b=(b+n)%(n+n)}
		if t==1{s.swap(a,b)}
		else{r=!r}
	}
	if r{s.rotate_right(n)}
	let s:String=s.into_iter().collect();
	println!("{}",s);
}