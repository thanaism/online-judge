use lazy_static::lazy_static;
use std::sync::Mutex;

lazy_static!{
    static ref H: Mutex<usize> = Mutex::new(0);
    static ref W: Mutex<usize> = Mutex::new(0);
    static ref V: Mutex<Vec<Vec<i32>>> = {
        let h = *H.lock().unwrap();
        let w = *W.lock().unwrap();
        let v = vec![vec![0;w];h];
        Mutex::new(v)
    };
}
fn main() {
    *H.lock().unwrap() = 5usize;
    *W.lock().unwrap() = 5usize;
    V.lock().unwrap()[0][1] = 500;
    sub();
    println!("{:?}",V.lock().unwrap());
}
fn sub() {
    // let vec = &mut *V.lock().unwrap();
    // let vec = &mut V.lock().unwrap();
    // let mut vec = V.lock().unwrap();
    print_type_of(&mut *V.lock().unwrap());
    // vec[1][1]=900;
    // vec[3][3]=350;
    // V.lock().unwrap()[0][2] = 1000;
    // V.lock().unwrap()[0][3] = 1000;
}
fn print_type_of<T>(_: T) {
    println!("{}", std::any::type_name::<T>());
}