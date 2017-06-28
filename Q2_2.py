"""
CENG 420 Assignment 2 Question 2.2

**********************************************
Andres Aburto   V00778603
Kunyu Zhang     V00784674
Xiang Xu        V00768356
Yangguang Liu   V00782918
**********************************************

****************************************************IMPORTANT****************************************************
This program is writen under Python 2.7, please make sure you have suitable Python version installed.

"""
"""
README

1.  Run the main program
    python Q2_2.py

2.  Enter the total item number (10, 15 or 20)

3.  The result will be displayed, including generated random data, best knapsack set, best weight used, best value
    carried and total calculation time.
"""
# Brute Force algorithm to solve knapsack problem

from random import random
import time

# header = ['id', 'weight', 'value']


# Generate n random items with [1,50] in weight and [10,100] in value
def generate_random_items(n = 10):
    items = []
    for i in range(n):
        items.append([i, 1+int(49*random()),10+int(90*random())])
    # print items
    return items


# Create every single set of possible results
def item_set(items):
    res = [[]]
    for item in items:
        new_set = [sets + [item] for sets in res]
        # print new_set
        res.extend(new_set)
    return res


# Implement brute force search to calculate the best solution
def brute_force(items, max_weight = 25):
    knapsack_set = []
    best_weight = 0
    best_value = 0
    for itemset in item_set(items):
        set_weight = sum(res[1] for res in itemset)
        set_value = sum(res[2] for res in itemset)
        if set_value > best_value and set_weight <= max_weight:
            best_weight = set_weight
            best_value = set_value
            knapsack_set = itemset
    return knapsack_set, best_weight, best_value


def main():
    num = input('Please enter the total item number (10, 15 or 20)')
    try:
        if not int(num) in [10, 15, 20]:
            print 'Input error, please input designated item number'
            return
    except:
        print 'Input Error. Please input designated item number'
    time_start = time.time()
    data = generate_random_items(num)
    # print item_set(data)
    if num == 10:
        max_weight = 25
    elif num == 15:
        max_weight = 35
    elif num == 20:
        max_weight = 50
    k, w, v = brute_force(data, max_weight)
    time_end = time.time()
    print 'generated data [id, weight, value]:', data
    print 'Best knapsack set:', k
    print 'Best weight used:', w
    print 'Best value carried:', v
    print 'The algorithm used %f seconds' % (time_end - time_start)


if __name__ == '__main__':
    main()