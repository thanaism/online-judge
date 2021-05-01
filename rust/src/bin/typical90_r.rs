use std::f64::consts::PI;
fn main() {
    proconio::input! {
        t:f64,
        l:f64, x:f64, y:f64,
        q:i64,
        e:[f64;q]
    }
    let l = l / 2.0;
    for i in &e {
        let rad = 2.0 * PI * i / t;
        let dy = -l * rad.sin();
        let dz = l * (1.0 - rad.cos());
        let dx = (x * x + (y - dy) * (y - dy)).sqrt();
        let deg = dz.atan2(dx) * 180.0 / PI;
        println!("{}", deg);
    }
}
