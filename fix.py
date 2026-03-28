with open('ai-hearing-navi.html', 'r') as f:
    c = f.read()

old = 'function onSpeech(txt){if(!cur||!N[cur])return;var n=N[cur],o=ovlp(txt,n.s);if(o>0.3){spk="staff";custTxt="";clrCd()}else if(txt.length>0){spk="customer";custTxt=txt;rstCd()}updBar()}'
new = 'var prevTxt="";function onSpeech(txt){if(!cur||!N[cur])return;var n=N[cur];var delta=txt.length>prevTxt.length?txt.slice(prevTxt.length):txt;prevTxt=txt;if(!delta||delta.trim().length<2)return;var o=ovlp(delta,n.s);if(o>0.25){spk="staff";custTxt="";clrCd()}else{spk="customer";custTxt=delta;rstCd()}updBar()}'

if old in c:
    c = c.replace(old, new)
    with open('ai-hearing-navi.html', 'w') as f:
        f.write(c)
    print('修正完了')
else:
    print('見つからない')
