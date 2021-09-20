def BubbleSort(c,n)
	(0...n).each {|i|
		(n-1).downto(i+1) {|j|
			if c[j][1].to_i < c[j-1][1].to_i
				tmp = c[j]
				c[j] = c[j-1]
				c[j-1] = tmp
			end
		}
	}
	return c
end

def SelectionSort(c,n)
	(0...n).each {|i|
		minj = i
		(i...n).each {|j|
			minj = j if c[j][1].to_i < c[minj][1].to_i
		}
        tmp = c[i]
		c[i] = c[minj]
		c[minj] = tmp
	}
	return c
end

n = gets.to_i
a = gets.split(" ")
b = a.sort_by{|x|x[1].to_i}
def print(x,y)
	puts x == y ? "Stable" : "Not stable"
end
ans = BubbleSort(a.dup,n)
puts ans.join(" ")
print(ans,b)
ans = SelectionSort(a.dup,n)
puts ans.join(" ")
print(ans,b)