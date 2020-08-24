import timeit
LOOPS = 5  # 計測回数を記載

def main():
  # ここに処理を記載

print(timeit.timeit('main()',globals=globals(),number=LOOPS)/LOOPS)