use std::collections::{BTreeMap, BTreeSet, HashMap, HashSet};
fn main() {
    let mut m1: BTreeMap<isize, isize> = BTreeMap::new();
    let mut m2: HashMap<isize, isize> = HashMap::new();
    let mut s1:BTreeSet<isize> = BTreeSet::new();
    let mut s2:HashSet<isize> = HashSet::new();
    m1.insert(1, 1);
    m1.insert(2, 1);
    m1.insert(5, 2);
    m1.insert(3, 2);
    m2.insert(1, 1);
    m2.insert(2, 1);
    m2.insert(5, 2);
    m2.insert(3, 2);
    s1.insert(100);
    s1.insert(80);
    s1.insert(120);
    s2.insert(100);
    s2.insert(80);
    s2.insert(120);
    println!("{:?}",m1);
    println!("{:?}",m2);
    println!("{:?}",s1);
    println!("{:?}",s2);
}
