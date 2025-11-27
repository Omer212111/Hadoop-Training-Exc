#!/usr/bin/env python
"""mapper.py"""

import sys

def read_input(file):
    for line in file:
        yield line.split()

def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            # 1. convert to lowercase
            word = word.lower()

            # 2. strip trailing commas and dots
            word = word.rstrip(".,")   

            # don't emit empty strings (can happen if line ends with . or ,)
            if word:
                print('%s%s%d' % (word, separator, 1))

if __name__ == "__main__":
    main()
