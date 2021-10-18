(d, g), *pc = *$<.map { |l| l.split.map &:to_i }
0.upto(d - 1) { |i| pc[i][1] /= 100 }

dp = Array.new(d + 1) { Array.new(1100, 0) }

for i in 1..d
  for j in 0...1100
    max_count = pc[i - 1][0]
    for k in 0..max_count
      if j - k > 0
        dp[i][j] = [
          dp[i - 1][j - k] + i * k + (k == max_count ? pc[i - 1][1] : 0),
          dp[i - 1][j],
        ].max
      end
    end
  end
end

ans = 1 << 60
for i in 1..d
  for j in 0...1100
    ans = [ans, j - 1].min if dp[i][j] >= g / 100
  end
end

p ans
