hello="childrenplayinginplayground"
half=(len(hello))//2
half_word=(hello[0:half]).upper()
half2=hello[half:]
full_word=half_word+half2
print(full_word)

  
f="dallen"
g=""
for n in f:
    if n not in g:
        g=g+n
print(g)
