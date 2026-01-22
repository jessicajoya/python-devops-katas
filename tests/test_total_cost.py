from katas.total_cost.total_cost import get_total_cost


def test_basic_case():
    costs = {"socks": 5, "shoes": 60, "sweater": 30}
    items = ["socks", "shoes"]
    assert get_total_cost(costs, items, 0.09) == 70.85


def test_ignore_unknown_items():
    costs = {"apple": 2}
    items = ["apple", "banana"]
    assert get_total_cost(costs, items, 0.10) == 2.2


def test_empty_items():
    costs = {"apple": 2}
    assert get_total_cost(costs, [], 0.10) == 0.0
