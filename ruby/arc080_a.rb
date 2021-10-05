n = gets.to_i
a = gets.split(" ").map(&:to_i)
four = a.map{|i|i%4==0 ? 1 : 0}.sum
two = a.map{|i|(i&1==0 && i%4 != 0) ? 1 : 0}.sum
no = a.map{|i|i&1==1 ? 1 : 0}.sum
if four+1==no && n==four+no
	ans = "Yes"
elsif four<no
	ans = "No"
else
	ans = "Yes"
end
puts ans