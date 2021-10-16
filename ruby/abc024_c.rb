(n,d,k),*lr=$<.map{|l|l.split.map &:to_i}
st=lr.pop k
puts st.map{|s,t|a=b=s;1+lr.index{|l,r|a=l if l<a&&a<=r;b=r if b<r&&l<=b;a<=t&&t<=b}}