#!/usr/bin/env python
"""reducer.py - Returns the 3 most frequent words from MapReduce output"""
 
from itertools import groupby
from operator import itemgetter
import sys
 
def read_mapper_output(file, separator='\t'):
    """Reads input from the mapper, expected format: 'word<separator>1'"""
    for line in file:
        # Split by the separator only once (to handle potential separators in the word itself)
        yield line.rstrip().split(separator, 1)
 
def main(separator='\t'):
    # Input comes from STDIN (standard input, which is the mapper's output)
    data = read_mapper_output(sys.stdin, separator=separator)
    
    # Dictionary to store the total counts for each word
    word_counts = {}
    
    # The groupby function groups all 'word-count' pairs by word
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            # Sum up all the counts for the current word
            # group is an iterator of ['word', 'count'] pairs
            total_count = sum(int(count) for word, count in group)
            # Store the total count in the dictionary
            word_counts[current_word] = total_count
        except ValueError:
            # count was not a number, silently discard this item
            pass
            
    
    # 1. Convert the dictionary into a list of tuples: (count, word)
    # We put the count first so that Python's sort function sorts by count.
    sorted_counts = [(count, word) for word, count in word_counts.items()]
    
    # 2. Sort the list in descending order (highest count first)
    sorted_counts.sort(reverse=True)
    
    # 3. Select the first three items (the Top 3)
    top_3 = sorted_counts[:3]
    
    # 4. Print the result
    # Removed the emoji from the introductory print statement.
    print("Top 3 Most Frequent Words:")
    for count, word in top_3:
        # Output format: word<separator>count
        print ("%s%s%d" % (word, separator, count))
 
if __name__ == "__main__":
    main()