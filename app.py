from flask import Flask, render_template, request

app = Flask(__name__)

# 固定起始值
GOLD_START = 80821
HM_START = 150
PU_START = 2094
HM_PRICE = 600
PU_PRICE = 50

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        gold_end = int(request.form["gold_end"])
        hm_end = int(request.form["hm_end"])
        pu_end = int(request.form["pu_end"])

        gold_gain = gold_end - GOLD_START
        hm_used = HM_START - hm_end
        pu_used = PU_START - pu_end
        hm_cost = hm_used * HM_PRICE
        pu_cost = pu_used * PU_PRICE
        total_cost = hm_cost + pu_cost
        net_profit = gold_gain - total_cost

        status = "✅ 有賺錢！" if net_profit > 0 else "❌ 有虧損！" if net_profit < 0 else "⚖️ 剛好打平。"

        result = {
            "gold_gain": gold_gain,
            "hm_used": hm_used,
            "pu_used": pu_used,
            "hm_cost": hm_cost,
            "pu_cost": pu_cost,
            "total_cost": total_cost,
            "net_profit": net_profit,
            "status": status
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
