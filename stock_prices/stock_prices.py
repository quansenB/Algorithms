#!/usr/bin/python

import argparse

def find_max_profit(prices):
  combinations = []
  for i in prices:
    priceIndex = prices.index(i)
    for j in range(priceIndex + 1, len(prices)):
      priceDifference = prices[j] - prices[priceIndex]
      combinations.append(priceDifference)
  return max(combinations)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))