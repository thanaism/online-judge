s = gets.chomp
base = "WBWBWWBWBWBW"
a = [(base*2)[0,20]]
11.times do
	base = base.chars.rotate(1).join
	a << (base*2)[0,20]
end

ans = ["Do","Do","Re","Re","Mi","Fa","Fa","So","So","La","La","Si"]
for i in 0..11
	if a[i]==s
		puts ans[i]
		break
	end
end