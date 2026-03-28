with open('ai-hearing-navi.html', 'r') as f:
    c = f.read()

# listenBtnを追加する新しいdrawMain
idx = c.find('function drawMain(n)')
print('drawMain見つかった:', idx > 0)
print(repr(c[idx:idx+100]))
