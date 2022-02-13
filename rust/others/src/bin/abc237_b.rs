fn main() {
    let (h, w) = {
        let line = read_line();
        let mut iter = line.split_whitespace();
        let h: usize = iter.next().unwrap().parse().unwrap();
        let w: usize = iter.next().unwrap().parse().unwrap();
        (h, w)
    };
    // println!("{} {}", h, w);
    let a: Vec<Vec<usize>> = {
        let vec: Vec<Vec<usize>> = (0..h)
            .map(|_| {
                let line = read_line();
                let mut iter = line.split_whitespace();
                let vec: Vec<usize> = (0..w)
                    .map(|_| iter.next().unwrap().parse::<usize>().unwrap())
                    .collect();
                vec
            })
            .collect();
        vec
    };
    for i in 0..w {
        for j in 0..h {
            if j != h - 1 {
                print!("{} ", a[j][i]);
            } else {
                println!("{}", a[j][i]);
            }
        }
    }
}

#[allow(dead_code)]
fn read_string() -> String {
    use std::io::Read;
    let mut buffer = String::new();
    std::io::stdin().read_to_string(&mut buffer).unwrap();
    buffer
}

fn read_line() -> String {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).unwrap();
    buffer.trim_end().to_owned()
}
