use proconio::{input,marker::Usize1};

struct Edge {
    u: usize,
    v: usize,
    cost: isize,
}

struct Kruskal {
    uf: UnionFind,
    total: isize,
    edges: Vec<Edge>,
}

impl Kruskal {
    fn init(vec: Vec<Edge>, vmax: usize) -> isize {
        let mut krs = Kruskal {
            uf: UnionFind::new(vmax),
            total: 0,
            edges: vec,
        };
        krs.edges.sort_by(|a, b| a.cost.cmp(&b.cost));
        for e in krs.edges {
            if !krs.uf.same(e.u, e.v) {
                krs.uf.join(e.u, e.v);
                if e.cost>0 {krs.total += e.cost}
            }
        }
        krs.total
    }
}

struct UnionFind { p: Vec<isize>, }

impl UnionFind {
    fn new(n: usize) -> UnionFind {
        UnionFind { p: vec![-1; n] }
    }
    fn join(&mut self, x: usize, y: usize) {
        let mut i = self.root(x);
        let mut j = self.root(y);
        if i == j { return; }
        if i > j { i=i^j; j=i^j; i=i^j; }
        self.p[i] += self.p[j];
        self.p[j] = i as isize;
    }

    fn root(&mut self, x: usize) -> usize {
        if self.p[x] < 0 { return x }
        self.p[x] = self.root(self.p[x] as usize) as isize;
        self.p[x] as usize
    }

    fn same(&mut self, x: usize, y: usize) -> bool {
        self.root(x) == self.root(y)
    }
}

fn main() {
    input!{
		n:usize,
		m:usize,
		ls:[(Usize1,Usize1,isize);m]
	}
    // println!("{} {} {:?}",n,m,ls);
    let mut edges = Vec::new();
    let mut append = |x, y, z| {
        edges.push(Edge { u: x, v: y, cost: z })
    };
	let mut total = 0isize;
	for i in 0..m {
		let cost = ls[i].2;
		append(ls[i].0,ls[i].1,cost);
		if cost>0 {total += ls[i].2}
	}
    let krs = Kruskal::init(edges, n);
    println!("{}", total-krs);
}
