# Listing_23-2.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Rolling two 6-sided dice 1,000 times

import random

totals = [0, 0]
totals1 = ['正面', '反面']

for i in range(1200000):
    result = random.choice(totals1)
    print(result)
    if result == totals1[0]:
        totals[0] += 1
    else:
        totals[1] += 1
