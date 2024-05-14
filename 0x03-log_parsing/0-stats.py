#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""

import sys
from collections import defaultdict

cache = defaultdict(int)
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache:
                cache[code] += 1
            total_size += size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size:', total_size)
            for key, value in sorted(cache.items()):
                if value != 0:
                    print(f'{key}: {value}')

except KeyboardInterrupt:
    pass

finally:
    print('File size:', total_size)
    for key, value in sorted(cache.items()):
        if value != 0:
            print(f'{key}: {value}')
