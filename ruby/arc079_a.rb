n,m = gets.split(" ").map(&:to_i)
l = Array.new(n){Array.new}
m.times{
	a,b = gets.split(" ").map(&:to_i)
	a-=1;b-=1
	l[a] << b
	l[b] << a
}
q = [0]
d = Array.new(n,-1)
d[0] = 0
while !q.empty?
	i = q.pop
	for j in l[i]
		if d[j]==-1 && !(j==n-1 && d[i]==0)
			d[j] = d[i]+1
			q.unshift j
		end
	end
end
ans = d[n-1]!=2 ? "IMPOSSIBLE" : "POSSIBLE"
puts ans
