use proconio::input;
use std::collections::{VecDeque,HashMap,HashSet};

fn encode(x:usize,y:usize)->usize {
    let i;
    let j;
    if x > y {
        i = x; j = y;
    } else {
        i = y; j = x;
    }
    i*(i-1)/2 + j+1
}

fn decode(n:usize)->HashMap<usize,Vec<usize>> {
    let mut indexes: HashMap<usize,Vec<usize>> = HashMap::new();
    for i in 1..=n {
        for j in (i+1)..=n {
            let k = encode(i,j);
            *indexes.entry(k).or_default() = vec![i,j];
        }
    }
    return indexes;
}

fn gen_graph(n: usize,
             a: Vec<Vec<usize>>,
             endpoints: &mut HashMap<usize,Vec<usize>>,
             indegrees: &mut HashMap<usize,usize>
            ) {
    for i in 0..n {
        for j in 1..n-1 {
            let s = i+1;
            let t = a[i][j-1];
            let u = a[i][j];
            let x = encode(s,t);
            let y = encode(s,u);
            endpoints.entry(x).or_insert(Vec::new()).push(y);
            *indegrees.entry(y).or_insert(0) += 1;
        }
    }
}

fn init_queue(n:usize,
              indegrees: &mut HashMap<usize,usize>
            )->VecDeque<usize> {
    let mut q = VecDeque::new();
    for i in 1..=n {
        for j in (i+1)..=n {
            let k = encode(i, j);
            if !indegrees.contains_key(&k) {
                q.push_back(k);
            }
        }
    }
    return q;
}

fn topological_sort(n: usize,
                    indexes: &HashMap<usize,Vec<usize>>,
                    q: &mut VecDeque<usize>,
                    indegrees: &mut HashMap<usize,usize>,
                    endpoints: &mut HashMap<usize,Vec<usize>>
                ) {
    let mut s: HashSet<usize> = HashSet::new();
    let mut cnt = 0usize;
    let mut ans = 1usize;
    while !q.is_empty() {
        let i = q.pop_front().unwrap();
        let x = indexes[&i][0];
        let y = indexes[&i][1];
        if s.contains(&x) || s.contains(&y) {
            s = HashSet::new();
            ans += 1;
        }
        s.insert(x);
        s.insert(y);
        cnt += 1;
        if !endpoints.contains_key(&i) {continue}
        for j in &endpoints[&i] {
            *indegrees.entry(*j).or_insert(0) -= 1;
            if indegrees[&j]==0 {q.push_back(*j)}
        }
    }

    if n*(n-1)/2 > cnt {println!("{}",-1);}
    else{println!("{}",ans);}
}

fn main() {
    input!{
        n: usize,
        a: [[usize;n-1];n]
    }

    let indexes = decode(n);

    let mut endpoints: HashMap<usize,Vec<usize>> = HashMap::new();
    let mut indegrees: HashMap<usize, usize> = HashMap::new();
    gen_graph(n, a, &mut endpoints, &mut indegrees);

    let mut q = init_queue(n, &mut indegrees);
    topological_sort(n, &indexes, &mut q, &mut indegrees, &mut endpoints);
}