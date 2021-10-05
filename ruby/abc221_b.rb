s=gets
t=gets
ans="No"
ans="Yes" if s==t
for i in 1...s.length
	s[i-1],s[i] = s[i],s[i-1]
	ans="Yes" if s==t
	s[i-1],s[i] = s[i],s[i-1]
end
puts ans