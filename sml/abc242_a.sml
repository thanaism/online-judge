fun readReal () = TextIO.scanStream Real.scan TextIO.stdIn ;
val SOME a = readReal () ;
val SOME b = readReal () ;
val SOME c = readReal () ;
val SOME x = readReal () ;
val ans = if x<=a then 1.0 else if x>b then 0.0 else c/(b-a) ;
print (Real.toString ans) ;