n = gets.to_i
a = gets.split(" ").map(&:to_i)
flag = true
count = 0
while flag do
  flag = false
  (n-1).downto(1) {|j|
    if a[j] < a[j-1]
      tmp=a[j]
      a[j]=a[j-1]
      a[j-1]=tmp
      count += 1
      flag = true
    end
    }
end
puts a.join(" ")
puts count