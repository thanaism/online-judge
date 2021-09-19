n = gets.to_i
l = []
n.times {l.push(gets.to_i)}
mi = [l[0]]
(1...n).each {|i|
  mi.push([mi[-1],l[i]].min)
}
ans=-(1 << 60)
(1...n).each {|i|
  ans = [ans,l[i]-mi[i-1]].max
}
puts ans
