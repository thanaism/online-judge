import 'dart:io';

void main() async {
  final s = stdin.readLineSync() ?? "";
  final ab = stdin.readLineSync()?.split(" ").map(int.parse);
  int a = (ab?.first ?? 0) - 1;
  int b = (ab?.last ?? 0) - 1;
  String ans = s.substring(0, a) +
      s[b] +
      s.substring(a + 1, b) +
      s[a] +
      s.substring(b + 1, s.length);
  print(ans);
}
