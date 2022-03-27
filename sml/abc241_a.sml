fun readInt () = TextIO.scanStream (Int.scan StringCvt.DEC) TextIO.stdIn ;
val a = List.tabulate (10, fn _ => valOf (readInt ())) ;
val n = List.nth(a,List.nth(a,List.nth(a,0))) ;
print (Int.toString n) ;