with open('ai-hearing-navi.html', 'r') as f:
    c = f.read()

# rec.onendでrestartしてるのが原因 - 止める
old = 'rec.onend=function(){if(on){try{rec.start()}catch(x){}}};'
new = 'rec.onend=function(){};'

if old in c:
    c = c.replace(old, new)
    with open('ai-hearing-navi.html', 'w') as f:
        f.write(c)
    print('修正完了')
else:
    print('見つからない')
    idx = c.find('rec.onend')
    print(repr(c[idx:idx+80]))
