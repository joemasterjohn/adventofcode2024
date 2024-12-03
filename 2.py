#!/usr/bin/env python

import sys

valid_range = range(1, 4)

# Part 1
def safe(l):
  if l[0] < l[1]:
    return all([l[i+1] - l[i] in valid_range for i in range(len(l)-1)])
  else:
    return all([l[i] - l[i+1] in valid_range for i in range(len(l)-1)])

# Part 2
def really_safe(l):
  for i in range(len(l)):
    if safe(l[0:i] + l[i+1:]):
      return True
  return False

data = list(list(int(i) for i in l.split()) for l in sys.stdin.readlines())

print(sum(1 if safe(l) else 0 for l in data))
print(sum(1 if really_safe(l) else 0 for l in data))
