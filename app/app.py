    <div class="card"><div class="jersey">19</div><div class="player-name">Pau Víctor</div><div class="player-country"><span class="flag">🇪 🇸 </span>Spain</div><span class="pos-tag fwd">FWD</span></div>
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


