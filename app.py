from flask import Flask, render_template, request

app = Flask(__name__)


def calculate_flip(purchase_price, rehab_cost, sale_price, holding_costs, selling_cost_rate=0.06):
    """
    Calculates the basic financial results of a house flip.
    It adds the main costs together, estimates selling costs, and returns
    total cost, profit, and ROI so the deal can be evaluated clearly.
    """
    selling_costs = sale_price * selling_cost_rate
    total_cost = purchase_price + rehab_cost + holding_costs + selling_costs
    profit = sale_price - total_cost

    if total_cost > 0:
        roi = (profit / total_cost) * 100
    else:
        roi = 0

    return total_cost, profit, roi


@app.route("/")
def home():
    """
    Shows the home page with the deal input form.
    """
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    """
    Gets the deal inputs from the form, runs the flip calculations,
    and sends the results to the results page.
    """
    purchase_price = float(request.form["purchase_price"])
    rehab_cost = float(request.form["rehab_cost"])
    sale_price = float(request.form["sale_price"])
    holding_costs = float(request.form["holding_costs"])

    total_cost, profit, roi = calculate_flip(
        purchase_price,
        rehab_cost,
        sale_price,
        holding_costs
    )

    return render_template(
        "results.html",
        purchase_price=purchase_price,
        rehab_cost=rehab_cost,
        sale_price=sale_price,
        holding_costs=holding_costs,
        total_cost=total_cost,
        profit=profit,
        roi=roi
    )


if __name__ == "__main__":
    app.run(debug=True)