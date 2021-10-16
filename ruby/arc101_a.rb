n,k = gets.split(" ").map(&:to_i)
x = gets.split(" ").map(&:to_i)

left = []
right = []
x.each do |i|
	if i<0
		left << -i
	else
		right << i
	end
end

left.reverse!
nl = left.length
nr = right.length

ans = 1<<60
if nl==0
	nl,nr = nr,nl
	left,right = right,left
end
for i in 0...nl
	break if i + 1 > k
	ans = [ans,left[i]].min if i+1==k
	j = k - i - 2
	next if j<0 || j>=nr
	dl = left[i]
	dr = right[j]
	ans = [ans, dl+2*dr, 2*dl+dr].min
end

p ans
