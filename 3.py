import re
import sys

inputs = ''.join(sys.stdin.readlines())

# Part 1
pattern = r"mul\((?P<a>[0-9]{1,3}),(?P<b>[0-9]{1,3})\)"

matches = re.finditer(pattern, inputs)
s = 0
for match in matches:
  s += int(match.group('a'))*int(match.group('b'))

print(s)

# Part 2
do_dnt_mul = r"(?P<do>do\(\))|(?P<dnt>don't\(\))|(?P<mul>mul\((?P<a>[0-9]{1,3}),(?P<b>[0-9]{1,3})\))"
matches = re.finditer(do_dnt_mul, inputs)

s = 0
count = True
for match in matches:
  if match.group("do") != None:
    count = True 
  elif match.group("dnt") != None:
    count = False
  elif match.group("mul") != None:
    if count:
      s += int(match.group('a'))*int(match.group('b'))
print(s)
