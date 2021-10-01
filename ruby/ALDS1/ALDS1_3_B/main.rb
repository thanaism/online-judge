n,q = gets.split(" ").map(&:to_i)
que = Queue.new
n.times do
	p,t = gets.split(" ")
	t = t.to_i
	que << [p,t]
end

ans = 0 
while !que.empty? do
	p,t = que.pop()
	d = t-q
	if d > 0
		ans += q
		que << [p,d]
	else
		ans += t
		puts [p,ans]*" "
	end
end
