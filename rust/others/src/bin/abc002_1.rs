fn main() {
    proconio::input! {x:isize,y:isize}
    println!("{}", if x > y { x } else { y })
}
