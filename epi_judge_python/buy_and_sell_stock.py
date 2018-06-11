from test_framework import generic_test
import sys

def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    max_profit, min_price = 0.0, sys.maxsize
    for price in prices:
        profit = price - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, price)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
