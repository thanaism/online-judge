use proconio::input;
struct UnionFind { p: Vec<isize> }

impl UnionFind {
    fn new(n:usize) -> UnionFind { UnionFind{ p:vec![-1;n]} }
    fn join(&mut self,x:usize,y:usize) {
        let mut i = self.root(x);
        let mut j = self.root(y);
        if i==j { return }
        if i>j { i=i^j; j=i^j; i=i^j; }
        self.p[i]+=self.p[j];
        self.p[j]=i as isize;
    }

    fn root(&mut self,x:usize) -> usize {
        if self.p[x] < 0 { return x }
        self.p[x] = self.root(self.p[x] as usize) as isize;
        self.p[x] as usize
    }

    fn same(&mut self,x:usize,y:usize) -> bool {
        self.root(x) == self.root(y)
    }
}


fn main() {
    input!{
        n:usize,
        m:usize,
        ab:[(Usize1,Usize1);m],
    }
    let mut uf = UnionFind::new(n);
    let mut dic = std::collections::HashMap::new();
    for a,b in ab {
        if uf.same(a,b) {
            println!("{}","No");
            return;
        }
        uf.join(a,b);
        *dic.entry(a).or_insert(0) += 1;
        if *dic.entry(a).or_insert(0) > 2 {
            println!("{}","No");
            return;
        }
        *dic.entry(b).or_insert(0) += 1;
        if *dic.entry(b).or_insert(0) > 2 {
            println!("{}","No");
            return;
        }
    }
}
