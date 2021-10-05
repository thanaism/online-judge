x = gets.to_i
n = (x+10)/11
if n*11 - x > 4
	ans = n * 2 -1
else
	ans = n*2
end
puts ans