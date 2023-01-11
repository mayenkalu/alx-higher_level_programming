#!/usr/bin/python3
""" Defines a script that read stdin line by line."""


import sys
from collections import defaultdict

line_count = 0
total_size = 0
status_codes = defaultdict(int)

try:
    for line in sys.stdin:
    """Print accumulated metrics.
    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
        line_count += 1
        fields = line.strip().split()
        status_code = fields[-2]
        file_size = int(fields[-1])

        total_size += file_size
        status_codes[status_code] += 1

        if line_count % 10 == 0:
            print("Total file size: ", total_size)
            print("Number of lines by status code:")
            for status_code in sorted(status_codes.keys()):
                print(status_code + ": " + str(status_codes[status_code]))

except KeyboardInterrupt:
    print("Total file size: ", total_size)
    print("Number of lines by status code:")
    for status_code in sorted(status_codes.keys()):
        print(status_code + ": " + str(status_codes[status_code]))
