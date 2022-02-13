use proconio::input;
use std::cmp::Reverse;
use std::collections::BinaryHeap;

fn main() {
    input! {
        n: usize,
        k: usize,
        p: [usize; n],
    }
    let mut heap = BinaryHeap::new();
    for i in 0..k {
        heap.push(Reverse(p[i].to_owned()));
    }
    let mut now = heap.pop().unwrap().0;
    println!("{:?}", now);
    for i in k..n {
        if p[i] > now {
            heap.push(Reverse(p[i].to_owned()));
            now = heap.pop().unwrap().0;
        }
        println!("{:?}", now);
    }
}
