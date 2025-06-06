from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    potion_names = {
        "red": "紅色藥水",
        "orange": "橘色藥水",
        "white": "白色藥水",
        "blue": "藍色藥水",
        "energy": "活力藥水",
        "hotdog": "熱狗堡"
    }

    if request.method == "POST":
        try:
            gold_start = int(request.form.get("gold_start", 0))
            gold_end = int(request.form.get("gold_end", 0))
            gold_gain = gold_end - gold_start
        except:
            gold_start, gold_end, gold_gain = 0, 0, 0

        selected = request.form.getlist("potions")
        total_cost = 0
        potion_results = []

        for key in selected:
            try:
                start = int(request.form.get(f"{key}_start", 0))
                end = int(request.form.get(f"{key}_end", 0))
                price = int(request.form.get(f"{key}_price", 0))
                used = start - end
                cost = used * price
            except:
                used, cost = 0, 0

            total_cost += cost
            potion_results.append({
                "name": potion_names.get(key, key),
                "used": used,
                "cost": cost
            })

        net_profit = gold_gain - total_cost
        status = "✅ 有賺錢！" if net_profit > 0 else "❌ 有虧損！" if net_profit < 0 else "⚖️ 剛好打平。"

        result = {
            "gold_gain": gold_gain,
            "total_cost": total_cost,
            "net_profit": net_profit,
            "status": status,
            "potions": potion_results
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)