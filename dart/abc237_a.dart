import 'dart:io';

void main() {
  int N = int.parse(stdin.readLineSync() ?? "0");
  if (N >= -1 << 31 && N < 1 << 31) {
    print('Yes');
  } else {
    print('No');
  }
}
