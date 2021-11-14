for c in {a..f}; do
    find ./ -name "abc*_$c.py" -d 1 | xargs -I{} mv {} ./abc-$c/
done

for c in {a..b}; do
    find ./ -name "agc*_$c.py" -d 1 | xargs -I{} mv {} ./agc-$c/
done

for c in {a..d}; do
    find ./ -name "arc*_$c.py" -d 1 | xargs -I{} mv {} ./arc-$c/
done