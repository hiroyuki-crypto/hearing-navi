with open('ai-hearing-navi.html', 'r') as f:
    c = f.read()

old = 'function onSpeech(txt){if(!cur||!N[cur])return;var n=N[cur],o=ovlp(txt,n.s);if(o>0.3){spk="staff";custTxt="";clrCd()}else if(txt.length>0){if(spk==="staff"){spk="customer";stopMic();liveTxt="";custTxt="";setTimeout(startMic,300)}else{spk="customer";custTxt=txt;rstCd()}}updBar()}'

new = 'var staffEndPos=0;function onSpeech(txt){if(!cur||!N[cur])return;var n=N[cur];var fresh=txt.slice(staffEndPos);var o=ovlp(fresh,n.s);if(o>0.3){spk="staff";staffEndPos=txt.length;custTxt="";clrCd()}else if(fresh.trim().length>2){spk="customer";custTxt=fresh;rstCd()}updBar()}'

if old in c:
    c = c.replace(old, new)
    with open('ai-hearing-navi.html', 'w') as f:
        f.write(c)
    print('修正完了')
else:
    print('見つからない - 現在のonSpeech:')
    idx = c.find('function onSpeech')
    print(repr(c[idx:idx+400]))
