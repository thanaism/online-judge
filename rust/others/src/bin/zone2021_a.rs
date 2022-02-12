fn main() {
    proconio::input! {s:String}
    println!("{}", s.matches("ZONe").collect::<Vec<_>>().len());
}
// fn main(){let s:String=text_io::read!();println!("{}",s.matches("ZONe").collect::<Vec<_>>().len());}
// fn main(){println!("{}",whiteread::parse_line::<String>().unwrap().matches("ZONe").collect::<Vec<_>>().len());}
