n=gets.to_i
d=Hash.new(0)
n.times {
	a,b=gets.split(" ").map(&:to_i)
  d[a]+=1
  d[a+b]-=1
}
d = d.sort
pre_key, pre_val = d[0]
ans=Array.new(n+1,0)
for i in 1...d.length
  key, val = d[i]
  ans[pre_val] += key - pre_key
  pre_val += val
  pre_key = key
end
puts ans[1..]*" "