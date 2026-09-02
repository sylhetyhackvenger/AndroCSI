import json,time,math,random,shutil,threading,subprocess,statistics,socket
from collections import deque
from datetime import datetime
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer

N="AndroCSI"
A="SYLHETYHACKVENGER (THE-ERROR808)"
P=8080
L=threading.Lock()

S={"name":N,"author":A,"boot":time.time(),"status":"ONLINE","signal":-75,"average":-75,"variance":0.0,"volatility":0.0,"activity":"CALIBRATING","activity_score":0,"networks":[],"history":deque(maxlen=360),"activity_history":deque(maxlen=360),"events":deque(maxlen=150),"scan_count":0,"source":"INITIALIZING","csi":"CSI INPUT NOT CONNECTED","sensors":{},"battery":{}}

def X(x):
    return shutil.which(x) is not None

def J(c):
    if not X(c):
        return None
    try:
        return json.loads(subprocess.check_output([c],stderr=subprocess.DEVNULL,timeout=8).decode(errors="ignore"))
    except:
        return None

def E(m,t="INFO"):
    with L:
        S["events"].appendleft({"time":datetime.now().strftime("%H:%M:%S"),"type":t,"message":str(m)[:160]})

def R(x):
    try:
        return round(max(.5,min(999,10**((-50-float(x))/22))),1)
    except:
        return 0.0

def W():
    d=J("termux-wifi-scaninfo")
    if not isinstance(d,list):
        return []
    z=[]
    for i,x in enumerate(d):
        try:
            r=int(x.get("level",x.get("rssi",-100)))
        except:
            r=-100
        z.append({"id":i,"ssid":x.get("ssid") or "HIDDEN","bssid":x.get("bssid") or "UNKNOWN","signal":r,"frequency":x.get("frequency",0),"range":R(r),"security":x.get("capabilities","UNKNOWN")})
    return sorted(z,key=lambda q:q["signal"],reverse=True)

def Q():
    z={}
    q=J("termux-sensor")
    b=J("termux-battery-status")
    if q is not None:
        z["raw_sensor_data"]=q
    if b is not None:
        z["battery"]=b
    return z,b or {}

def C(h,vo):
    a=[x["value"] for x in h[-32:]]
    if len(a)<10:
        return "CALIBRATING",0
    d=[abs(a[i]-a[i-1]) for i in range(1,len(a))]
    md=sum(d)/max(1,len(d))
    peak=max(d) if d else 0
    recent=a[-7:]
    spread=max(recent)-min(recent)
    if peak>=9 and vo>=4:
        if spread<4:
            return "POSSIBLE FALL",95
        return "IMPACT EVENT",88
    if md<1 and vo<2:
        return "STILL / SITTING-LIKE",12
    if md<2.3:
        return "LOW ACTIVITY",30
    if md<4.3:
        return "WALKING-LIKE",58
    return "FAST WALKING-LIKE",82

def G():
    p=-72
    tick=0
    while True:
        try:
            n=W()
            if n:
                v=max(x["signal"] for x in n)
                u="TERMUX WIFI API"
            else:
                v=max(-95,min(-30,p+random.randint(-3,3)))
                u="NO WIFI SCAN API"
            with L:
                old=list(S["history"])
            a=[x["value"] for x in old[-48:]]
            av=sum(a)/len(a) if a else v
            vr=statistics.pvariance(a) if len(a)>1 else 0.0
            vo=math.sqrt(vr)
            ac,sc=C(old,vo)
            sn,bt=Q()
            with L:
                S["signal"]=v
                S["average"]=round(av,2)
                S["variance"]=round(vr,2)
                S["volatility"]=round(vo,2)
                S["activity"]=ac
                S["activity_score"]=sc
                S["networks"]=n
                S["history"].append({"time":time.time(),"value":v})
                S["activity_history"].append({"time":time.time(),"value":sc})
                S["scan_count"]+=1
                S["source"]=u
                S["sensors"]=sn
                S["battery"]=bt
            if abs(v-p)>=9:
                E("Rapid Wi-Fi signal disturbance","WATCH")
            if ac=="POSSIBLE FALL" and tick%5==0:
                E("Abrupt signal pattern classified as possible fall","ALERT")
            if tick%15==0:
                E("Signal environment analysis refreshed","INFO")
            p=v
            tick+=1
        except Exception as e:
            E(e,"ERROR")
        time.sleep(1)

H=r'''<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AndroCSI</title>
<style>
*{box-sizing:border-box}
:root{--c:#00dfff;--bg:#010405;--panel:#06131a}
body{margin:0;background:var(--bg);color:#ddfbff;font-family:Consolas,monospace;overflow-x:hidden}
body:before{content:"";position:fixed;inset:0;pointer-events:none;opacity:.12;background-image:linear-gradient(#00dfff20 1px,transparent 1px),linear-gradient(90deg,#00dfff20 1px,transparent 1px);background-size:42px 42px}
header{padding:18px 4%;display:flex;justify-content:space-between;align-items:center;background:linear-gradient(90deg,#010405,#06212b,#010405);border-bottom:1px solid var(--c)}
h1{margin:0;font-size:clamp(34px,8vw,78px);letter-spacing:10px;color:white;text-shadow:0 0 15px var(--c),0 0 50px #0088ff}
small{color:var(--c);letter-spacing:2px}#author{text-align:right;font-size:11px;line-height:1.6}
nav{position:sticky;top:0;z-index:9;text-align:center;padding:9px;background:#02090d;border-bottom:1px solid #07586b}
button{font:inherit;letter-spacing:1px;color:#bfffff;background:#061720;border:1px solid #087c94;padding:10px 13px;margin:2px;cursor:pointer}
button:hover,button.on{background:var(--c);color:#001015;box-shadow:0 0 20px var(--c)}
main{max-width:1700px;margin:auto;padding:16px}.page{display:none}.page.on{display:block;animation:in .3s ease}@keyframes in{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:13px}.card{position:relative;overflow:hidden;background:#061119e8;border:1px solid #087087;padding:17px;min-height:140px;box-shadow:inset 0 0 30px #00aaff0d,0 0 25px #00779918}
.label{font-size:10px;letter-spacing:3px;color:var(--c)}.big{font-size:clamp(27px,4vw,48px);margin-top:23px;color:white;text-shadow:0 0 14px var(--c)}
canvas{width:100%;height:330px;background:#02090d;border:1px solid #07576a;margin-top:13px}
#radar{position:relative;width:min(92vw,720px);aspect-ratio:1;margin:20px auto;border-radius:50%;overflow:hidden;border:2px solid #008ca8;background:repeating-radial-gradient(circle,#001117 0 1px,transparent 2px 20%),linear-gradient(45deg,transparent 49.8%,#00dfff33 50%,transparent 50.2%),linear-gradient(-45deg,transparent 49.8%,#00dfff33 50%,transparent 50.2%);box-shadow:inset 0 0 90px #00bfff22,0 0 55px #0088ff22}
#sweep{position:absolute;inset:-5%;background:conic-gradient(from 0deg,#00ffff66,transparent 13%,transparent 72%);animation:r 3s linear infinite}@keyframes r{to{transform:rotate(360deg)}}
.dot{position:absolute;width:13px;height:13px;border-radius:50%;transform:translate(-50%,-50%);z-index:3}.device{background:#030303;border:1px solid #555;box-shadow:0 0 8px #111}.person{background:#009dff;box-shadow:0 0 12px #00aaff,0 0 32px #00dfff;animation:p 1s infinite}@keyframes p{50%{transform:translate(-50%,-50%) scale(1.8)}}
#activity{text-align:center;font-size:clamp(22px,5vw,48px);color:#00bfff;text-shadow:0 0 25px #0088ff;padding:12px}
table{width:100%;border-collapse:collapse;margin-top:15px;font-size:12px}th,td{padding:9px;border-bottom:1px solid #0a4655;text-align:left}th{color:var(--c)}.event{margin:6px 0;padding:10px;border-left:3px solid var(--c);background:#051017;font-size:12px}.alert{border-left-color:#ff5050}.watch{border-left-color:#ffc34d}.error{border-left-color:#ff5050}
.note{color:#ffcf7b;line-height:1.7;font-size:12px}pre{white-space:pre-wrap;word-break:break-word;color:#aefaff}
@media(max-width:700px){header{flex-direction:column;text-align:center}#author{text-align:center;margin-top:10px}}
</style>
</head>
<body>
<header>
<div><h1>ANDROCSI</h1><small>WI-FI SIGNAL INTELLIGENCE • ACTIVITY ANALYSIS • SENSOR HUD</small></div>
<div id="author">AUTHOR<br>SYLHETYHACKVENGER<br>(THE-ERROR808)</div>
</header>
<nav>
<button class="on" onclick="P('dash',this)">COMMAND</button>
<button onclick="P('rad',this)">RADAR</button>
<button onclick="P('net',this)">NETWORKS</button>
<button onclick="P('sig',this)">SIGNAL</button>
<button onclick="P('water',this)">WATERFALL</button>
<button onclick="P('sonic',this)">SONIC</button>
<button onclick="P('sensors',this)">SENSORS</button>
<button onclick="P('events',this)">EVENTS</button>
<button onclick="P('system',this)">SYSTEM</button>
</nav>
<main>
<section id="dash" class="page on"><div class="grid">
<div class="card"><div class="label">PRIMARY SIGNAL</div><div class="big" id="rssi">--</div></div>
<div class="card"><div class="label">ROLLING AVERAGE</div><div class="big" id="avg">--</div></div>
<div class="card"><div class="label">SIGNAL VOLATILITY</div><div class="big" id="vol">--</div></div>
<div class="card"><div class="label">WI-FI ACTIVITY</div><div class="big" id="act">--</div></div>
<div class="card"><div class="label">ACTIVITY INDEX</div><div class="big" id="score">--</div></div>
<div class="card"><div class="label">NETWORK COUNT</div><div class="big" id="count">0</div></div>
</div><canvas id="live"></canvas></section>

<section id="rad" class="page"><div class="card"><div class="label">LIVE ACTIVITY RADAR</div><div id="activity">CALIBRATING</div><div id="radar"><div id="sweep"></div></div><p class="note">Blue dot: activity classification marker. Dark dots: discovered Wi-Fi radios/networks. Positions are visual estimates, not verified physical locations.</p></div><canvas id="motion"></canvas></section>

<section id="net" class="page"><div class="card"><div class="label">DISCOVERED WI-FI ENVIRONMENT</div><table><thead><tr><th>SSID</th><th>BSSID</th><th>RSSI</th><th>FREQ</th><th>RANGE</th><th>SECURITY</th></tr></thead><tbody id="tbl"></tbody></table></div></section>

<section id="sig" class="page"><div class="card"><div class="label">SIGNAL MATRIX</div><canvas id="signal"></canvas></div><div class="grid"><div class="card"><div class="label">VARIANCE</div><div class="big" id="variance">--</div></div><div class="card"><div class="label">SCAN COUNT</div><div class="big" id="scans">0</div></div><div class="card"><div class="label">SOURCE</div><div class="big" id="source">--</div></div></div></section>

<section id="water" class="page"><div class="card"><div class="label">LIVE SIGNAL WATERFALL</div><canvas id="waterfall"></canvas></div></section>

<section id="sonic" class="page"><div class="grid"><div class="card"><div class="label">WI-FI TO SOUND</div><div class="big" id="hz">0 Hz</div><br><button onclick="AUDIO()">START SONIFICATION</button><button onclick="STOPAUDIO()">STOP</button></div><div class="card"><div class="label">LOCAL MICROPHONE ACTIVITY</div><div class="big" id="micstate">MIC OFF</div><br><button onclick="MIC()">ENABLE MICROPHONE</button><button onclick="STOPMIC()">STOP MIC</button></div></div><canvas id="wave"></canvas></section>

<section id="sensors" class="page"><div class="card"><div class="label">DEVICE SENSOR / BATTERY DATA</div><pre id="sensorData">NO DATA</pre></div></section>

<section id="events" class="page"><div class="card"><div class="label">LIVE EVENT TIMELINE</div><div id="eventList"></div></div></section>

<section id="system" class="page"><div class="grid"><div class="card"><div class="label">SYSTEM STATUS</div><div class="big" id="status">--</div></div><div class="card"><div class="label">CSI STATUS</div><div class="big" id="csi">--</div></div><div class="card"><div class="label">UPTIME</div><div class="big" id="uptime">--</div></div></div><div class="card"><p class="note">Walking-like, fast-walking-like, sitting-like and possible-fall labels are heuristic interpretations of signal variation. Real CSI-based recognition requires compatible hardware and actual CSI measurements.</p><button onclick="SAVE()">EXPORT SNAPSHOT</button></div></section>
</main>

<script>
let D=null,AC=null,OSC=null,GAIN=null,MS=null,AN=null,person=null,wf=[],micActivity=null,lastMic=[],$=x=>document.getElementById(x)

function P(id,b){document.querySelectorAll(".page").forEach(x=>x.classList.remove("on"));$(id).classList.add("on");document.querySelectorAll("nav button").forEach(x=>x.classList.remove("on"));b.classList.add("on")}
function esc(x){return String(x??"").replace(/[&<>"]/g,m=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[m]))}
function CV(id){let c=$(id),r=c.getBoundingClientRect(),z=devicePixelRatio||1;c.width=r.width*z;c.height=r.height*z;let x=c.getContext("2d");x.setTransform(z,0,0,z,0,0);return[x,r.width,r.height]}
function LINE(id,data,min,max){let[x,w,h]=CV(id);x.clearRect(0,0,w,h);if(!data||data.length<2)return;x.strokeStyle="#00dfff";x.shadowColor="#00dfff";x.shadowBlur=12;x.beginPath();data.forEach((p,i)=>{let px=i/(data.length-1)*w,py=h-(Math.max(min,Math.min(max,p.value))-min)/(max-min)*h;i?x.lineTo(px,py):x.moveTo(px,py)});x.stroke();x.shadowBlur=0}
function RADAR(){let r=$("radar");r.querySelectorAll(".dot").forEach(x=>x.remove());if(!D)return;D.networks.forEach((n,i)=>{let a=i*137.508*Math.PI/180,d=Math.min(42,9+(Math.abs(n.signal+30)/70)*34),e=document.createElement("div");e.className="dot device";e.style.left=50+Math.cos(a)*d+"%";e.style.top=50+Math.sin(a)*d+"%";e.title=n.ssid;r.appendChild(e)});if(person){let e=document.createElement("div");e.className="dot person";e.style.left=person.x+"%";e.style.top=person.y+"%";r.appendChild(e)}}
function POS(){person={x:22+Math.random()*56,y:22+Math.random()*56};RADAR()}
function WATER(){let[x,w,h]=CV("waterfall");if(!D)return;wf.push(D.history.slice(-100).map(q=>q.value));wf=wf.slice(-Math.floor(h/4));x.clearRect(0,0,w,h);for(let y=0;y<wf.length;y++)for(let i=0;i<wf[y].length;i++){let v=Math.max(0,Math.min(1,(wf[y][i]+100)/70));x.fillStyle=`hsl(${190-v*190},100%,${18+v*48}%)`;x.fillRect(i*w/wf[y].length,h-(y+1)*4,w/wf[y].length+1,4)}}
function DRAW(){if(!D)return;LINE("live",D.history,-100,-30);LINE("signal",D.history,-100,-30);LINE("motion",D.activity_history,0,100);WATER()}
function UI(){if(!D)return;$("rssi").textContent=D.signal+" dBm";$("avg").textContent=D.average+" dBm";$("vol").textContent=D.volatility;$("act").textContent=micActivity?micActivity.name:D.activity;$("score").textContent=micActivity?micActivity.score+"%":D.activity_score+"%";$("count").textContent=D.networks.length;$("variance").textContent=D.variance;$("scans").textContent=D.scan_count;$("source").textContent=D.source;$("status").textContent=D.status;$("csi").textContent=D.csi;$("uptime").textContent=Math.floor(Date.now()/1000-D.boot)+"s";$("activity").textContent=micActivity?micActivity.name:D.activity;$("hz").textContent=Math.round(120+Math.max(0,Math.min(1,(D.signal+100)/70))*900)+" Hz";$("sensorData").textContent=JSON.stringify(D.sensors,null,2);$("tbl").innerHTML=D.networks.map(n=>`<tr><td>${esc(n.ssid)}</td><td>${esc(n.bssid)}</td><td>${n.signal} dBm</td><td>${n.frequency} MHz</td><td>~${n.range} m</td><td>${esc(n.security)}</td></tr>`).join("")||'<tr><td colspan="6">NO WI-FI SCAN DATA</td></tr>';$("eventList").innerHTML=D.events.map(e=>`<div class="event ${String(e.type).toLowerCase()}"><b>${e.time}</b> [${e.type}] ${esc(e.message)}</div>`).join("");RADAR();DRAW()}
async function GET(){try{D=await fetch("/api/state").then(x=>x.json());UI();SOUND()}catch(e){$("status").textContent="CONNECTION LOST"}}
function AUDIO(){AC=AC||new AudioContext();if(OSC)return;OSC=AC.createOscillator();GAIN=AC.createGain();OSC.type="sine";GAIN.gain.value=.035;OSC.connect(GAIN);GAIN.connect(AC.destination);OSC.start()}
function STOPAUDIO(){try{OSC&&OSC.stop()}catch(e){}OSC=null}
function SOUND(){if(!D||!OSC)return;OSC.frequency.setTargetAtTime(120+Math.max(0,Math.min(1,(D.signal+100)/70))*900,AC.currentTime,.1)}
async function MIC(){try{MS=await navigator.mediaDevices.getUserMedia({audio:true});AC=AC||new AudioContext();let src=AC.createMediaStreamSource(MS);AN=AC.createAnalyser();AN.fftSize=1024;src.connect(AN);$("micstate").textContent="LISTENING";MLOOP()}catch(e){$("micstate").textContent="MIC DENIED"}}
function STOPMIC(){if(MS)MS.getTracks().forEach(t=>t.stop());MS=null;AN=null;micActivity=null;person=null;$("micstate").textContent="MIC OFF"}
function MLOOP(){if(!AN)return;let a=new Uint8Array(AN.fftSize);AN.getByteTimeDomainData(a);let v=0;for(let q of a){let z=(q-128)/128;v+=z*z}v=Math.sqrt(v/a.length);lastMic.push({t:performance.now(),v});lastMic=lastMic.filter(x=>performance.now()-x.t<3500);let r=lastMic.slice(-12).map(x=>x.v),av=r.reduce((x,y)=>x+y,0)/Math.max(1,r.length),name="QUIET",score=5;if(v>.28&&v>av*2.2){name="IMPACT / POSSIBLE FALL";score=95}else if(v>.055&&av>.03&&lastMic.length>18){name="FAST WALKING-LIKE";score=80}else if(v>.018&&lastMic.length>12){name="WALKING-LIKE";score=58}else if(v>=.012){name="LOW ACTIVITY";score=28}micActivity={name,score};if(score>25)POS();if(name==="QUIET")person=null;$("micstate").textContent=name;DRAW_WAVE(a);UI();requestAnimationFrame(MLOOP)}
function DRAW_WAVE(a){let[x,w,h]=CV("wave");x.clearRect(0,0,w,h);x.strokeStyle="#00dfff";x.shadowColor="#00dfff";x.shadowBlur=10;x.beginPath();a.forEach((v,i)=>{let px=i/(a.length-1)*w,py=v/255*h;i?x.lineTo(px,py):x.moveTo(px,py)});x.stroke();x.shadowBlur=0}
function SAVE(){let b=new Blob([JSON.stringify(D,null,2)],{type:"application/json"}),a=document.createElement("a");a.href=URL.createObjectURL(b);a.download="androcsi-"+Date.now()+".json";a.click();URL.revokeObjectURL(a.href)}
setInterval(GET,1200);GET();addEventListener("resize",()=>{if(D)UI()})
</script>
</body>
</html>'''

class Z(BaseHTTPRequestHandler):
    def log_message(self,*x):
        pass

    def do_GET(self):
        if self.path=="/api/state":
            with L:
                d=dict(S)
                d["history"]=list(S["history"])
                d["activity_history"]=list(S["activity_history"])
                d["events"]=list(S["events"])
            b=json.dumps(d,default=list).encode()
            self.send_response(200)
            self.send_header("Content-Type","application/json")
            self.send_header("Content-Length",str(len(b)))
            self.end_headers()
            self.wfile.write(b)
            return
        b=H.encode()
        self.send_response(200)
        self.send_header("Content-Type","text/html; charset=utf-8")
        self.send_header("Content-Length",str(len(b)))
        self.end_headers()
        self.wfile.write(b)

def find_free_port(start_port):
    """Find a free port starting from start_port"""
    port = start_port
    while port < start_port + 100:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('127.0.0.1', port))
                return port
        except OSError:
            port += 1
    return None

E("AndroCSI initialized")
threading.Thread(target=G,daemon=True).start()

# Find available port
available_port = find_free_port(P)
if available_port is None:
    print("ERROR: No available ports found in range!")
    exit(1)

print(f"{N} | {A}")
print(f"OPEN: http://127.0.0.1:{available_port}")
print(f"(Port {P} was busy, using {available_port} instead)")

try:
    ThreadingHTTPServer(("127.0.0.1", available_port), Z).serve_forever()
except KeyboardInterrupt:
    print("\nShutting down...")
    pass
