def max_profit(prices: list[int]) -> int:
    lowest = prices[0]
    profit = 0
    for p in prices[1:]:
        lowest = min(lowest, p)
        profit = max(profit, p - lowest)
    return profit


def test_max_profit():
    prices = [10, 1, 5, 6, 7, 1]
    assert max_profit(prices) == 6

    prices = [10, 8, 7, 5, 2]
    assert max_profit(prices) == 0


if __name__ == "__main__":
    test_max_profit()
