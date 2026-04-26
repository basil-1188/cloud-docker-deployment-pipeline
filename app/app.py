from flask import Flask, jsonify
import datetime

app = Flask(__name__)

HTML = open('/dev/stdin').read() if False else """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>FC Barcelona Squad 2025/26</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{background:#07080f;color:#e8e6e0;font-family:'Segoe UI',sans-serif;overflow-x:hidden;}
body::before{content:'';position:fixed;inset:0;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E");pointer-events:none;z-index:0;opacity:0.5;}
.hero{position:relative;padding:80px 24px 60px;text-align:center;overflow:hidden;z-index:1;}
.hero-bg{position:absolute;inset:0;background:linear-gradient(135deg,#001f5c 0%,#6b0028 50%,#001f5c 100%);z-index:0;}
.hero-bg::after{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 0%,rgba(0,77,159,0.6),transparent 60%),radial-gradient(ellipse at 80% 100%,rgba(165,0,68,0.5),transparent 50%);}
.hero-stripes{position:absolute;inset:0;background:repeating-linear-gradient(45deg,transparent,transparent 40px,rgba(255,255,255,0.015) 40px,rgba(255,255,255,0.015) 80px);}
.hero-content{position:relative;z-index:1;}
.barca-badge{display:inline-flex;align-items:center;gap:10px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);border-radius:100px;padding:8px 20px;font-size:12px;letter-spacing:0.1em;margin-bottom:20px;animation:fadeDown 0.6s ease both;}
.badge-dot{width:8px;height:8px;background:#ffb400;border-radius:50%;animation:blink 1.5s ease infinite;box-shadow:0 0 8px #ffb400;}
@keyframes blink{0%,100%{opacity:1;transform:scale(1);}50%{opacity:0.3;transform:scale(0.7);}}
.hero h1{font-size:clamp(40px,8vw,88px);font-weight:900;letter-spacing:-2px;line-height:1;animation:fadeDown 0.6s ease 0.1s both;}
.hero h1 .grad{background:linear-gradient(135deg,#60a5fa,#f87171);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.hero-sub{color:rgba(255,255,255,0.6);font-size:15px;margin-top:10px;margin-bottom:36px;letter-spacing:0.05em;animation:fadeDown 0.6s ease 0.2s both;}
.hero-stats{display:flex;justify-content:center;gap:0;flex-wrap:wrap;border-top:1px solid rgba(255,255,255,0.1);padding-top:32px;margin-top:32px;animation:fadeDown 0.6s ease 0.3s both;}
.hstat{padding:0 32px;text-align:center;position:relative;}
.hstat:not(:last-child)::after{content:'';position:absolute;right:0;top:20%;bottom:20%;width:1px;background:rgba(255,255,255,0.15);}
.hstat-n{font-size:30px;font-weight:900;color:#fff;}
.hstat-l{font-size:10px;color:rgba(255,255,255,0.5);text-transform:uppercase;letter-spacing:0.1em;margin-top:2px;}
@keyframes fadeDown{from{opacity:0;transform:translateY(-20px);}to{opacity:1;transform:translateY(0);}}
.container{max-width:1140px;margin:0 auto;padding:64px 20px;position:relative;z-index:1;}
.sec-header{margin-bottom:24px;display:flex;align-items:center;gap:14px;}
.sec-line{height:1px;flex:1;background:linear-gradient(90deg,rgba(255,255,255,0.1),transparent);}
.sec-label{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:0.14em;padding:4px 14px;border-radius:100px;white-space:nowrap;}
.lbl-gk{background:rgba(255,180,0,0.1);color:#ffb400;border:1px solid rgba(255,180,0,0.25);}
.lbl-def{background:rgba(96,165,250,0.1);color:#60a5fa;border:1px solid rgba(96,165,250,0.25);}
.lbl-mid{background:rgba(52,211,153,0.1);color:#34d399;border:1px solid rgba(52,211,153,0.25);}
.lbl-fwd{background:rgba(248,113,113,0.1);color:#f87171;border:1px solid rgba(248,113,113,0.25);}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px;margin-bottom:56px;}
.card{background:#0f1420;border:1px solid rgba(255,255,255,0.06);border-radius:20px;padding:28px 20px 22px;text-align:center;transition:all 0.4s cubic-bezier(0.23,1,0.32,1);position:relative;overflow:hidden;opacity:0;transform:translateY(24px);}
.card.visible{opacity:1;transform:translateY(0);}
.card::before{content:'';position:absolute;inset:0;background:radial-gradient(circle at var(--mx,50%) var(--my,50%),var(--glow,rgba(96,165,250,0.06)),transparent 65%);opacity:0;transition:opacity 0.4s;}
.card::after{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--accent,linear-gradient(90deg,#60a5fa,#34d399));transform:scaleX(0);transition:transform 0.4s cubic-bezier(0.23,1,0.32,1);}
.card:hover{transform:translateY(-8px) scale(1.02);border-color:rgba(255,255,255,0.12);box-shadow:0 24px 60px rgba(0,0,0,0.5);}
.card:hover::before{opacity:1;}
.card:hover::after{transform:scaleX(1);}
.avatar{width:72px;height:72px;border-radius:50%;margin:0 auto 14px;display:flex;align-items:center;justify-content:center;font-size:19px;font-weight:900;letter-spacing:-0.5px;position:relative;transition:all 0.4s;}
.card:hover .avatar{transform:scale(1.12);}
.avatar::before{content:'';position:absolute;inset:-3px;border-radius:50%;background:var(--ring,conic-gradient(#60a5fa,#a78bfa,#60a5fa));z-index:-1;animation:spin 4s linear infinite;opacity:0;transition:opacity 0.4s;}
.card:hover .avatar::before{opacity:1;}
@keyframes spin{to{transform:rotate(360deg);}}
.av-gk{background:linear-gradient(135deg,#78350f,#d97706);color:#fef3c7;--ring:conic-gradient(#f59e0b,#fbbf24,#f59e0b);--glow:rgba(245,158,11,0.08);--accent:linear-gradient(90deg,#f59e0b,#fbbf24);}
.av-def{background:linear-gradient(135deg,#1e3a8a,#2563eb);color:#dbeafe;--ring:conic-gradient(#3b82f6,#93c5fd,#3b82f6);--glow:rgba(59,130,246,0.08);--accent:linear-gradient(90deg,#3b82f6,#93c5fd);}
.av-mid{background:linear-gradient(135deg,#064e3b,#059669);color:#d1fae5;--ring:conic-gradient(#10b981,#6ee7b7,#10b981);--glow:rgba(16,185,129,0.08);--accent:linear-gradient(90deg,#10b981,#6ee7b7);}
.av-fwd{background:linear-gradient(135deg,#7f1d1d,#dc2626);color:#fee2e2;--ring:conic-gradient(#ef4444,#fca5a5,#ef4444);--glow:rgba(239,68,68,0.08);--accent:linear-gradient(90deg,#ef4444,#fca5a5);}
.player-name{font-size:14px;font-weight:700;color:#fff;margin-bottom:5px;line-height:1.3;}
.player-country{font-size:12px;color:#64748b;margin-bottom:12px;}
.flag{font-size:15px;margin-right:3px;}
.card-footer{display:flex;align-items:center;justify-content:center;gap:8px;}
.jnum{font-size:11px;font-weight:700;color:rgba(255,255,255,0.25);font-family:monospace;}
.pos-tag{font-size:10px;font-weight:700;padding:2px 9px;border-radius:100px;letter-spacing:0.06em;}
.pos-gk{background:rgba(255,180,0,0.1);color:#ffb400;border:1px solid rgba(255,180,0,0.2);}
.pos-def{background:rgba(59,130,246,0.1);color:#60a5fa;border:1px solid rgba(59,130,246,0.2);}
.pos-mid{background:rgba(16,185,129,0.1);color:#34d399;border:1px solid rgba(16,185,129,0.2);}
.pos-fwd{background:rgba(239,68,68,0.1);color:#f87171;border:1px solid rgba(239,68,68,0.2);}
footer{border-top:1px solid rgba(255,255,255,0.06);padding:28px 20px;text-align:center;position:relative;z-index:1;}
footer p{font-size:12px;color:#374151;}
footer span{color:#a50044;font-weight:600;}
::-webkit-scrollbar{width:3px;}
::-webkit-scrollbar-track{background:#07080f;}
::-webkit-scrollbar-thumb{background:linear-gradient(#004d9f,#a50044);border-radius:2px;}
@media(max-width:600px){.hstat{padding:0 14px;}.grid{grid-template-columns:1fr 1fr;}.card{padding:20px 12px 16px;}.avatar{width:56px;height:56px;font-size:15px;}}
</style>
</head>
<body>
<div class="hero">
  <div class="hero-bg"></div>
  <div class="hero-stripes"></div>
  <div class="hero-content">
    <div class="barca-badge"><span class="badge-dot"></span>2025 / 26 Season &nbsp;&bull;&nbsp; La Liga</div>
    <h1>FC <span class="grad">Barcelona</span></h1>
    <p class="hero-sub">Mes que un club &nbsp;&bull;&nbsp; More than a club &nbsp;&bull;&nbsp; Spotify Camp Nou</p>
    <div class="hero-stats">
      <div class="hstat"><div class="hstat-n">26</div><div class="hstat-l">Players</div></div>
      <div class="hstat"><div class="hstat-n">1899</div><div class="hstat-l">Founded</div></div>
      <div class="hstat"><div class="hstat-n">27</div><div class="hstat-l">La Liga Titles</div></div>
      <div class="hstat"><div class="hstat-n">5</div><div class="hstat-l">UCL Titles</div></div>
      <div class="hstat"><div class="hstat-n">#1</div><div class="hstat-l">La Liga 25/26</div></div>
    </div>
  </div>
</div>
<div class="container">
  <div class="sec-header"><span class="sec-label lbl-gk">Goalkeepers</span><div class="sec-line"></div></div>
  <div class="grid">
    <div class="card"><div class="avatar av-gk">JG</div><div class="player-name">Joan Garcia</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><div class="card-footer"><span class="jnum">#13</span><span class="pos-tag pos-gk">GK</span></div></div>
    <div class="card"><div class="avatar av-gk">AA</div><div class="player-name">Wojciech Szczęsny</div><div class="player-country"><span class="flag">🇵🇱</span>Poland</div><div class="card-footer"><span class="jnum">#25</span><span class="pos-tag pos-gk">GK</span></div></div>
        <div class="card"><div class="avatar av-gk">MTS</div><div class="player-name">Diego Kochen</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><div class="card-footer"><span class="jnum">#31</span><span class="pos-tag pos-gk">GK</span></div></div>
  </div>
  <div class="sec-header"><span class="sec-label lbl-def">Defenders</span><div class="sec-line"></div></div>
  <div class="grid">
    <div class="card"><div class="avatar av-def">HF</div><div class="player-name">Andreas Christensen</div><div class="player-country"><span class="flag">🇩🇰</span>Denmark</div><div class="card-footer"><span class="jnum">#15</span><span class="pos-tag pos-def">DEF</span></div></div>
    <div class="card"><div class="avatar av-def">AB</div><div class="player-name">Alejandro Balde</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><div class="card-footer"><span class="jnum">#3</span><span class="pos-tag pos-def">DEF</span></div></div>
    <div class="card"><div class="avatar av-def">RA</div><div class="player-name">Ronald Araújo</div><div class="player-country"><span class="flag">🇺🇾</span>Uruguay</div><div class="card-footer"><span class="jnum">#4</span><span class="pos-tag pos-def">DEF</span></div></div>
    <div class="card"><div class="avatar av-def">PC</div><div class="player-name">Pau Cubarsí</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><div class="card-footer"><span class="jnum">#5</span><span class="pos-tag pos-def">DEF</span></div></div>
    <div class="card"><div class="avatar av-def">GM</div><div class="player-name">Gerard Martín</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><div class="card-footer"><span class="jnum">#18</span><span class="pos-tag pos-def">DEF</span></div></div>
    <div class="card"><div class="avatar av-def">JK</div><div class="player-name">Jules Koundé</div><div class="player-country"><span class="flag">🇫🇷</span>France</div><div class="card-footer"><span class="jnum">#23</span><span class="pos-tag pos-def">DEF</span></div></div>
    <div class="card"><div class="avatar av-def">EG</div><div class="player-name">Eric García</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><div class="card-footer"><span class="jnum">#24</span><span class="pos-tag pos-def">DEF</span></div></div>
        <div class="card"><div class="avatar av-def">EG</div><div class="player-name">Joao Cancelo</div><div class="player-country"><span class="flag">ᵖʳ</span>Portugal</div><div class="card-footer"><span class="jnum">#2</span><span class="pos-tag pos-def">DEF</span></div></div>
  </div>
  <div class="sec-header"><span class="sec-label lbl-mid">Midfielders</span><div class="sec-line"></div></div>
  <div class="grid">
    <div class="card"><div class="avatar av-mid">GA</div><div class="player-name">Gavi</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><div class="card-footer"><span class="jnum">#6</span><span class="pos-tag pos-mid">MID</span></div></div>
    <div class="card"><div class="avatar av-mid">PE</div><div class="player-name">Pedri</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><div class="card-footer"><span class="jnum">#8</span><span class="pos-tag pos-mid">MID</span></div></div>
    <div class="card"><div class="avatar av-mid">AC</div><div class="player-name">Andreas Christensen</div><div class="player-country"><span class="flag">🇩🇰</span>Denmark</div><div class="card-footer"><span class="jnum">#15</span><span class="pos-tag pos-mid">MID</span></div></div>
    <div class="card"><div class="avatar av-mid">FL</div><div class="player-name">Fermín López</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><div class="card-footer"><span class="jnum">#16</span><span class="pos-tag pos-mid">MID</span></div></div>
    <div class="card"><div class="avatar av-mid">DO</div><div class="player-name">Dani Olmo</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><div class="card-footer"><span class="jnum">#20</span><span class="pos-tag pos-mid">MID</span></div></div>
    <div class="card"><div class="avatar av-mid">FDJ</div><div class="player-name">Frenkie de Jong</div><div class="player-country"><span class="flag">🇳🇱</span>Netherlands</div><div class="card-footer"><span class="jnum">#21</span><span class="pos-tag pos-mid">MID</span></div></div>
    <div class="card"><div class="avatar av-mid">FK</div><div class="player-name">Marc Casadó</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><div class="card-footer"><span class="jnum">#17</span><span class="pos-tag pos-mid">MID</span></div></div>
    <div class="card"><div class="avatar av-mid">MB</div><div class="player-name">Marc Bernal</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><div class="card-footer"><span class="jnum">#22</span><span class="pos-tag pos-mid">MID</span></div></div>
  </div>
  <div class="sec-header"><span class="sec-label lbl-fwd">Forwards</span><div class="sec-line"></div></div>
  <div class="grid">
    <div class="card"><div class="avatar av-fwd">FT</div><div class="player-name">Ferran Torres</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><div class="card-footer"><span class="jnum">#7</span><span class="pos-tag pos-fwd">FWD</span></div></div>
    <div class="card"><div class="avatar av-fwd">RL</div><div class="player-name">Robert Lewandowski</div><div class="player-country"><span class="flag">🇵🇱</span>Poland</div><div class="card-footer"><span class="jnum">#9</span><span class="pos-tag pos-fwd">FWD</span></div></div>
    <div class="card"><div class="avatar av-fwd">LY</div><div class="player-name">Lamine Yamal</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><div class="card-footer"><span class="jnum">#10</span><span class="pos-tag pos-fwd">FWD</span></div></div>
    <div class="card"><div class="avatar av-fwd">RA</div><div class="player-name">Raphinha</div><div class="player-country"><span class="flag">🇧🇷</span>Brazil</div><div class="card-footer"><span class="jnum">#11</span><span class="pos-tag pos-fwd">FWD</span></div></div>
    <div class="card"><div class="avatar av-fwd">MR</div><div class="player-name">Marcus Rashford</div><div class="player-country"><span class="flag">🏴󠁧󠁢󠁥󠁮󠁧󠁿</span>England</div><div class="card-footer"><span class="jnum">#14</span><span class="pos-tag pos-fwd">FWD</span></div></div>
    <div class="card"><div class="avatar av-fwd">PV</div><div class="player-name">Roony Bardghji</div><div class="player-country"><span class="flag">sw</span>Sweden</div><div class="card-footer"><span class="jnum">#19</span><span class="pos-tag pos-fwd">FWD</span></div></div>
  </div>
</div>
<footer><p>FC Barcelona Squad 2025/26 &nbsp;·&nbsp; Deployed on <span>AWS EC2</span> via <span>Docker + GitHub Actions CI/CD</span> &nbsp;·&nbsp; Built by Basil MK</p></footer>
<script>
const obs=new IntersectionObserver(entries=>{entries.forEach((e,i)=>{if(e.isIntersecting){setTimeout(()=>e.target.classList.add('visible'),i*60);obs.unobserve(e.target);}});},{threshold:0.05});
document.querySelectorAll('.card').forEach(c=>obs.observe(c));
document.querySelectorAll('.card').forEach(card=>{card.addEventListener('mousemove',e=>{const r=card.getBoundingClientRect();card.style.setProperty('--mx',((e.clientX-r.left)/r.width*100)+'%');card.style.setProperty('--my',((e.clientY-r.top)/r.height*100)+'%');});});
</script>
</body>
</html>"""

@app.route("/")
def home():
    return HTML

@app.route("/health")
def health():
    return jsonify({"status":"healthy","timestamp":datetime.datetime.now().isoformat()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
