n=gets.to_s
l=n.length
ans=0
for i in 0...(1<<l)
  a=String.new
  b=String.new
	for j in 0...l
    if (i>>j)&1==1
      a << n[j]
    else
      b << n[j]
    end
  end
  next if a.length==0 || b.length==0
  a = a.chars.sort.reverse.join.to_i
  b = b.chars.sort.reverse.join.to_i
  ans=[ans,a*b].max
end
puts ans