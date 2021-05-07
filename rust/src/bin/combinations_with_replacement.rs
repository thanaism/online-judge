fn main() {
//     let n = 5usize;
//     let r = 3usize;
//     // let mut pool:Vec<usize> = (0..n).collect();
//     // println!("{:?}",pool);
//     let mut pool:Vec<usize> = (0..n).collect();
//     // println!("{:?}",pool);
//     let mut indices = vec![0usize;r];
//     let mut hp:Vec<Vec<usize>> = vec![];
//     hp.push(indices.iter().map(|i|pool[*i]).collect());
//     let mut flg = true;
//     while flg {
//         let mut j:usize;
//         for i in (0..r).rev() {
//             if indices[i] != n-1 {  }
//             else { flg=false;break }
//         }
//         indices = indices.iter().enumerate().map(|(k,v)|if k>=i {*v+1} else {*v}).collect();
//         println!("{:?}",indices.iter().map(|i|pool[*i]).collect::<Vec<usize>>());
//     }
//     println!("{:?}",hp);
}
