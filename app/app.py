from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>FC Barcelona Squad 2025/26</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;}
body{background:#0a0a0f;color:#e8e6e0;font-family:'Segoe UI',sans-serif;}
.hero{background:linear-gradient(135deg,#004d9f 0%,#a50044 100%);padding:60px 20px;text-align:center;position:relative;overflow:hidden;}
.hero::before{content:'';position:absolute;inset:0;background:url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.03'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");}
.badge{display:inline-block;background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.2);border-radius:100px;padding:6px 18px;font-size:12px;letter-spacing:0.1em;margin-bottom:16px;}
.hero h1{font-size:clamp(32px,6vw,64px);font-weight:900;letter-spacing:-1px;margin-bottom:8px;}
.hero p{color:rgba(255,255,255,0.7);font-size:16px;margin-bottom:24px;}
.stats-row{display:flex;justify-content:center;gap:40px;flex-wrap:wrap;margin-top:32px;padding-top:28px;border-top:1px solid rgba(255,255,255,0.15);}
.stat{text-align:center;}
.stat-n{font-size:28px;font-weight:900;color:#fff;}
.stat-l{font-size:11px;color:rgba(255,255,255,0.6);text-transform:uppercase;letter-spacing:0.08em;}
.container{max-width:1100px;margin:0 auto;padding:60px 20px;}
.section-title{font-size:11px;font-weight:700;color:#a50044;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:20px;display:flex;align-items:center;gap:10px;}
.section-title::before{content:'';width:20px;height:1px;background:#a50044;}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px;margin-bottom:48px;}
.card{background:#111622;border:1px solid rgba(255,255,255,0.06);border-radius:16px;padding:20px;transition:all 0.3s;position:relative;overflow:hidden;}
.card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,#004d9f,#a50044);opacity:0;transition:opacity 0.3s;}
.card:hover{transform:translateY(-4px);border-color:rgba(165,0,68,0.3);box-shadow:0 16px 40px rgba(0,0,0,0.4);}
.card:hover::before{opacity:1;}
.jersey{font-size:36px;font-weight:900;background:linear-gradient(135deg,#004d9f,#a50044);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1;margin-bottom:8px;}
.player-name{font-size:15px;font-weight:700;color:#fff;margin-bottom:4px;}
.player-country{font-size:12px;color:#64748b;margin-bottom:10px;}
.pos-tag{display:inline-block;font-size:10px;font-weight:600;padding:3px 10px;border-radius:100px;letter-spacing:0.06em;}
.gk{background:rgba(255,180,0,0.1);color:#ffb400;border:1px solid rgba(255,180,0,0.2);}
.def{background:rgba(0,77,159,0.15);color:#60a5fa;border:1px solid rgba(0,77,159,0.3);}
.mid{background:rgba(16,185,129,0.1);color:#10b981;border:1px solid rgba(16,185,129,0.2);}
.fwd{background:rgba(165,0,68,0.15);color:#f87171;border:1px solid rgba(165,0,68,0.3);}
.flag{font-size:18px;margin-right:4px;}
footer{text-align:center;padding:28px;border-top:1px solid rgba(255,255,255,0.06);font-size:12px;color:#374151;}
footer span{color:#a50044;}
@media(max-width:600px){.stats-row{gap:20px;}.grid{grid-template-columns:1fr 1fr;}}
</style>
</head>
<body>
<div class="hero">
  <div class="badge">2025 / 26 Season</div>
  <h1>FC Barcelona</h1>
  <p>Mes que un club &nbsp;·&nbsp; More than a club</p>
  <div class="stats-row">
    <div class="stat"><div class="stat-n">26</div><div class="stat-l">Players</div></div>
    <div class="stat"><div class="stat-n">1899</div><div class="stat-l">Founded</div></div>
    <div class="stat"><div class="stat-n">27</div><div class="stat-l">La Liga Titles</div></div>
    <div class="stat"><div class="stat-n">5</div><div class="stat-l">UCL Titles</div></div>
  </div>
</div>

<div class="container">

  <div class="section-title">Goalkeepers</div>
  <div class="grid">
    <div class="card"><div class="jersey">1</div><div class="player-name">Marc-André ter Stegen</div><div class="player-country"><span class="flag">🇩🇪</span>Germany</div><span class="pos-tag gk">GK</span></div>
    <div class="card"><div class="jersey">13</div><div class="player-name">Joan Garcia</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><span class="pos-tag gk">GK</span></div>
    <div class="card"><div class="jersey">25</div><div class="player-name">Ander Astralaga</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><span class="pos-tag gk">GK</span></div>
  </div>

  <div class="section-title">Defenders</div>
  <div class="grid">
    <div class="card"><div class="jersey">2</div><div class="player-name">Héctor Fort</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><span class="pos-tag def">DEF</span></div>
    <div class="card"><div class="jersey">3</div><div class="player-name">Alejandro Balde</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><span class="pos-tag def">DEF</span></div>
    <div class="card"><div class="jersey">4</div><div class="player-name">Ronald Araújo</div><div class="player-country"><span class="flag">🇺🇾</span>Uruguay</div><span class="pos-tag def">DEF</span></div>
    <div class="card"><div class="jersey">5</div><div class="player-name">Pau Cubarsí</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><span class="pos-tag def">DEF</span></div>
    <div class="card"><div class="jersey">18</div><div class="player-name">Gerard Martín</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><span class="pos-tag def">DEF</span></div>
    <div class="card"><div class="jersey">23</div><div class="player-name">Jules Koundé</div><div class="player-country"><span class="flag">🇫🇷</span>France</div><span class="pos-tag def">DEF</span></div>
    <div class="card"><div class="jersey">24</div><div class="player-name">Eric García</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><span class="pos-tag def">DEF</span></div>
  </div>

  <div class="section-title">Midfielders</div>
  <div class="grid">
    <div class="card"><div class="jersey">6</div><div class="player-name">Gavi</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><span class="pos-tag mid">MID</span></div>
    <div class="card"><div class="jersey">8</div><div class="player-name">Pedri</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><span class="pos-tag mid">MID</span></div>
    <div class="card"><div class="jersey">15</div><div class="player-name">Andreas Christensen</div><div class="player-country"><span class="flag">🇩🇰</span>Denmark</div><span class="pos-tag mid">MID</span></div>
    <div class="card"><div class="jersey">16</div><div class="player-name">Fermín López</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><span class="pos-tag mid">MID</span></div>
    <div class="card"><div class="jersey">17</div><div class="player-name">Dani Olmo</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><span class="pos-tag mid">MID</span></div>
    <div class="card"><div class="jersey">20</div><div class="player-name">Frenkie de Jong</div><div class="player-country"><span class="flag">🇳🇱</span>Netherlands</div><span class="pos-tag mid">MID</span></div>
    <div class="card"><div class="jersey">21</div><div class="player-name">Franck Kessié</div><div class="player-country"><span class="flag">🇨🇮</span>Ivory Coast</div><span class="pos-tag mid">MID</span></div>
    <div class="card"><div class="jersey">22</div><div class="player-name">Marc Bernal</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><span class="pos-tag mid">MID</span></div>
  </div>

  <div class="section-title">Forwards</div>
  <div class="grid">
    <div class="card"><div class="jersey">7</div><div class="player-name">Ferran Torres</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><span class="pos-tag fwd">FWD</span></div>
    <div class="card"><div class="jersey">9</div><div class="player-name">Robert Lewandowski</div><div class="player-country"><span class="flag">🇵🇱</span>Poland</div><span class="pos-tag fwd">FWD</span></div>
    <div class="card"><div class="jersey">10</div><div class="player-name">Lamine Yamal</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><span class="pos-tag fwd">FWD</span></div>
    <div class="card"><div class="jersey">11</div><div class="player-name">Raphinha</div><div class="player-country"><span class="flag">🇧🇷</span>Brazil</div><span class="pos-tag fwd">FWD</span></div>
    <div class="card"><div class="jersey">14</div><div class="player-name">Marcus Rashford</div><div class="player-country"><span class="flag">🏴󠁧󠁢󠁥󠁮󠁧󠁿</span>England</div><span class="pos-tag fwd">FWD</span></div>
    <div class="card"><div class="jersey">19</div><div class="player-name">Pau Víctor</div><div class="player-country"><span class="flag">🇪🇸</span>Spain</div><span class="pos-tag fwd">FWD</span></div>
  </div>

</div>
<footer>FC Barcelona Squad 2025/26 &nbsp;·&nbsp; Deployed on <span>AWS EC2</span> via <span>Docker + GitHub Actions CI/CD</span></footer>
</body>
</html>
"""

@app.route("/health")
def health():
    import datetime
    from flask import jsonify
    return jsonify({"status":"healthy","timestamp":datetime.datetime.now().isoformat()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
