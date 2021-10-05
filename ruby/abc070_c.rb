n,*t = $<.map(&:to_i)

def gcd(x,y)
	return y if x==0
	gcd(y % x, x)
end

def lcm(x,y)
	x*y/gcd(x,y)
end

ans = t[0]
for i in 1...n
	ans = lcm(ans,t[i])
end

puts ans