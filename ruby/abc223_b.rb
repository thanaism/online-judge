s = gets.chomp.chars
n = s.length

a = []
0.upto(n){|i|a << s.rotate(i).join}
a.sort!

puts a.first,a.last