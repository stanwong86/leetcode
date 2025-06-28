'''
A man wants to rent an apartment in the city center. This man earns a euros per hour. Consider that he works for 6 hours per day for 5 days every week for four weeks. The apartment costs b euros per four weeks. You must also assume that you must consider spending c euros every four weeks for other reasons. It is necessary to produce "true" if he can afford the apartment or "false" if he can not.

In fact, it is pretty easy!
Good luck...
Input
Line 1: An integer a euro of profit per hour.
Line 2: An integer b the cost of the apartment per four weeks.
Line 3: An integer c other spending.
Output
Line 1: A string "true" or "false" if he can or cannot afford the apartment.
Constraints
Example
Input

42
1200
1400

Output

true

'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

earns_per_hour = int(input())
apartment_costs = int(input())
spending = int(input())


hours = 6
days = 5
weeks = 4
total_earnings = earns_per_hour * hours * days * weeks



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(str(total_earnings - apartment_costs - spending >= 0).lower())
