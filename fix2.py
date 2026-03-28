with open('ai-hearing-navi.html', 'r') as f:
    c = f.read()

# 部分一致で置き換え
old = 'else if(txt.length>0){spk="customer";custTxt=txt;rstCd()}updBar()}'
new = 'else if(txt.length>0){if(spk==="staff"){liveTxt="";custTxt="";spk="customer"}else{spk="customer";custTxt=txt;rstCd()}}updBar()}'

if old in c:
    c = c.replace(old, new)
    with open('ai-hearing-navi.html', 'w') as f:
        f.write(c)
    print('修正完了')
else:
    print('見つからない')
    idx = c.find('updBar()}')
    print(repr(c[idx-100:idx+20]))
