n=gets.to_i
a=[];b=[];c=[]
n.times{
  i,j=gets.split.map &:to_i
  a<<i;b<<j;c<<i.to_f/j
}
1.upto(n-1){|i|c[i]=c[i]+c[i-1]}
0.upto(n-1){|i|
  d=c[i]*2-c.last
  if d>=0
    p a[0..i].sum-d/2*b[i];exit
  end
}
