#!/usr/bin/env python

import sys

# Part 1

# Parse input
a, b = zip(*(x.split() for x in sys.stdin.readlines()))

# Convert and sort
a = sorted(int(x) for x in a)
b = sorted(int(x) for x in b)

print(sum(abs(x-y) for x,y in zip(a, b)))

# Part 2

total = 0

# O(n) time O(1) extra space solution (no dictionary lookup needed)
i, j = 0, 0
while i < len(a) and j < len(b):
  # Move forward in b until we hit an element >= a[i]
  while j < len(b) and a[i] > b[j]:
    j += 1
  count = 0
  # Count all of the identical elements in b (they will be contiguous)
  while j < len(b) and a[i] == b[j]:
    count += 1
    j += 1
  total += count * a[i]
  i += 1

print(total)
