import sys
import re

stdin = sys.stdin.read()
on = False
sum = 0
for match in re.finditer(r'([\+\-]?\d+|on|off|=)', stdin, re.IGNORECASE):
    if match.group(1).lower() == 'on' and not on:
        on = True
    elif match.group(1).lower() == 'off':
        on = False
    elif match.group(1) == '=':
        print(sum)
    elif on:
        sum += int(match.group(1))
