import urllib.request
urllib.request.urlretrieve("https://raw.githubusercontent.com/hiroyuki-crypto/hearing-navi/main/ai-hearing-navi.html", "/tmp/old.html")

new_html = open("/tmp/old.html").read()

# drawMain関数を丸ごと新しいボタン方式に置き換え
import re
new_draw = '''function drawMain(n){var ph=PH[n.p];ap.innerHTML=\'<div class="phase-bar"><div class="phase-info"><span class="phase-icon">\'+ph.ic+\'</span><div><div class="phase-num">フェーズ \'+n.p+\'</div><div class="phase-label" style="color:\'+ph.cl+\'">\'+ph.lb+\'</div></div></div><div class="progress">\'+[1,2,3,4].map(function(i){return\'<div class="progress-dot" style="background:\'+(i<=n.p?ph.cl:\'#3A3228\')+\'"></div>\'}).join("")+\'</div></div><div class="content">\'+(n.t?\'<div class="tone-hint">💡 \'+n.t+\'</div>\':\'\')+ \'<div class="card"><div class="card-label">お客様にこう伝えてください</div><div class="card-text">「\'+n.s+\'」</div></div>\'+(n.l?\'<div class="listen-hint">👂 聞きたいこと：<span>\'+n.l+\'</span></div>\':\'\')+ \'<button id="lb" style="background:#5E8B6A;color:#fff;border:none;border-radius:16px;padding:18px;font-size:17px;font-weight:700;width:100%;margin-top:8px;cursor:pointer">👂 お客様の返答を聞く</button></div><div class="status-bar"><div class="status-text" id="sTxt" style="background:#2C2418;border-radius:14px;padding:14px 16px;font-size:15px;line-height:1.8;color:#E8E0D4;min-height:52px;border:1px solid #3A3228">セリフを読み終えたら上のボタンを押してください</div><div class="countdown-bar" style="height:4px;background:#3A3228;border-radius:2px;margin-top:10px;overflow:hidden"><div id="cdFill" style="height:100%;background:#C4713B;width:0%;transition:width 0.1s"></div></div></div>\';document.getElementById("lb").onclick=function(){startListening()}}'''

# startListening関数も追加
new_start = '''var rec=null,listening=false,custTxt="",silTmr=null,cdPct=0,cdInt=null,WAIT=4000;
function startListening(){var SR=window.SpeechRecognition||window.webkitSpeechRecognition;if(!SR)return;if(rec){try{rec.stop()}catch(e){}}custTxt="";listening=true;var btn=document.getElementById("lb");if(btn){btn.textContent="🎤 聞いています…";btn.style.background="#C4713B"}try{rec=new SR();rec.lang="ja-JP";rec.interimResults=true;rec.continuous=true;rec.onresult=function(e){var t="";for(var i=0;i<e.results.length;i++){t+=e.results[i][0].transcript}custTxt=t;var el=document.getElementById("sTxt");if(el)el.textContent=t;clrCd();rstCd()};rec.onerror=function(e){};rec.onend=function(){if(listening){try{rec.start()}catch(x){}}};rec.start();rstCd()}catch(e){}}
function stopListening(){listening=false;if(rec){try{rec.stop()}catch(e){}}rec=null;clrCd()}
function rstCd(){clrCd();cdPct=100;var st=Date.now();cdInt=setInterval(function(){cdPct=Math.max(0,100-((Date.now()-st)/WAIT)*100);var f=document.getElementById("cdFill");if(f)f.style.width=cdPct+"%"},50);silTmr=setTimeout(function(){clrCd();if(custTxt.trim()){stopListening();adv(custTxt.trim())}},WAIT)}
function clrCd(){if(silTmr){clearTimeout(silTmr);silTmr=null}if(cdInt){clearInterval(cdInt);cdInt=null}cdPct=0;var f=document.getElementById("cdFill");if(f)f.style.width="0%"}'''

# 古い変数宣言とonSpeech系を置き換え
new_html = re.sub(r'var cur=null,rec=null.*?function ovlp', 'var cur=null;\n' + new_start + '\nfunction ovlp', new_html, flags=re.DOTALL)

# drawMainを置き換え
new_html = re.sub(r'function drawMain\(n\)\{.*?(?=function draw\(\))', new_draw + '\n', new_html, flags=re.DOTALL)

# startMic/stopMic/onSpeech/updBar削除は不要（上書きされてる）

with open("/Users/hiroyukitsuji/hearing-navi/ai-hearing-navi.html", "w") as f:
    f.write(new_html)
print("完了")
