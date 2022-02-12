import 'dart:io';
import 'dart:math';

void main() {
  int _ = int.parse(stdin.readLineSync() ?? "");
  List<int> a = stdin.readLineSync()?.split(" ").map(int.parse).toList() ?? [];
  List<int> cut = [0];
  int now = 0;
  a.forEach((element) {
    cut.add((now + element) % 360);
    now += element;
    now %= 360;
  });
  int ans = 0;
  cut.sort();
  for (int i = 1; i < cut.length; ++i) {
    ans = max(ans, cut[i] - cut[i - 1]);
  }
  ans = max(ans, 360 - cut.last);
  print(ans);
}
