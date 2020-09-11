import timeit
LOOPS = 5  # 計測回数を記載

def main():
  # ここに処理を記載

f=lambda:main()
print(f"{int(timeit.timeit(f,globals=globals(),number=LOOPS)/LOOPS*1000)} ms")