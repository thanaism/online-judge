def gcd(a,b)
	if a==0
		return b
	else
		return gcd(b%a,a)
	end
end
x,y = gets.split(" ").map(&:to_i)
puts gcd(x,y)