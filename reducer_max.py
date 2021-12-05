#!/usr/bin/env python3

import sys

def reducer():
    maxSales = 0
    oldKey = None

    for line in sys.stdin:
        data = line.strip().split(",")

        thisKey = data[0]
        thisCost = int(round(float(data[1])))
        if oldKey is not None and oldKey != thisKey:
            decimal_cost = str(float(maxSales - 0.01))
            print(oldKey + "," + decimal_cost)
            maxSales = thisCost

        oldKey = thisKey
        maxSales = max(maxSales, thisCost)

    if oldKey is not None: # for the final key
        decimal_cost = str(float(maxSales - 0.01))
        print (oldKey + "," + decimal_cost)

if __name__ == "__main__":
    # what function should run when python reducer.py is called?
    reducer()
