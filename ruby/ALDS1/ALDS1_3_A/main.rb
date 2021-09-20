commands = gets.split(" ")
stack = []
commands.each {|c|
	if /[0-9]+/===c
		stack.push(c.to_i)
	else
		b=stack.pop
		a=stack.pop
		stack.push(eval("#{a}#{c}#{b}"))
	end
}
puts stack.pop
