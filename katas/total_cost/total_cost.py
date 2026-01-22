def get_total_cost(costs: dict, items: list, tax: float) -> float:
    subtotal = 0

    for item in items:
        if item in costs:
            subtotal += costs[item]

    total = subtotal + (subtotal * tax)
    return round(total, 2)
