from flask import Flask, render_template, request
from services.listings_api import search_properties, get_property_by_id
from services.calculations import analyze_flip

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():
    location = request.args.get("location", "").strip()

    if not location:
        return render_template("results.html", location=location, properties=[])

    properties = search_properties(location)
    return render_template("results.html", location=location, properties=properties)


@app.route("/analyze/<int:property_id>", methods=["GET", "POST"])
def analyze(property_id):
    property_data = get_property_by_id(property_id)
    analysis = None

    if request.method == "POST":
        purchase_price = float(request.form.get("purchase_price", 0))
        rehab_cost = float(request.form.get("rehab_cost", 0))
        resale_value = float(request.form.get("resale_value", 0))
        extra_costs = float(request.form.get("extra_costs", 0))

        analysis = analyze_flip(
            purchase_price=purchase_price,
            rehab_cost=rehab_cost,
            resale_value=resale_value,
            extra_costs=extra_costs
        )

    return render_template("analysis.html", property=property_data, analysis=analysis)


if __name__ == "__main__":
    app.run(debug=True)