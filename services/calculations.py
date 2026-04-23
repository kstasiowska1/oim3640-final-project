def analyze_flip(purchase_price, rehab_cost, resale_value, extra_costs=0):
    total_cost = purchase_price + rehab_cost + extra_costs
    profit = resale_value - total_cost

    if total_cost > 0:
        roi = (profit / total_cost) * 100
    else:
        roi = 0

    if roi > 15:
        rating = "Strong Flip Opportunity"
        color_class = "strong"
    elif roi >= 8:
        rating = "Moderate Opportunity"
        color_class = "moderate"
    else:
        rating = "Risky Deal"
        color_class = "risky"

    return {
        "total_cost": total_cost,
        "profit": profit,
        "roi": roi,
        "rating": rating,
        "color_class": color_class
    }