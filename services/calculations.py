def analyze_flip(purchase_price, rehab_cost, resale_value, extra_costs=0):
    """
    Analyze a house flip deal and return key metrics.
    """

    total_cost = purchase_price + rehab_cost + extra_costs
    profit = resale_value - total_cost

    if total_cost > 0:
        roi = (profit / total_cost) * 100
    else:
        roi = 0

    if roi > 15:
        rating = "Strong Flip Opportunity"
    elif roi >= 8:
        rating = "Moderate Opportunity"
    else:
        rating = "Risky Deal"

    return {
        "total_cost": total_cost,
        "profit": profit,
        "roi": roi,
        "rating": rating
    }