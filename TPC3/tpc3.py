import sys
import re

stdin = sys.stdin.read()
on = False
sum = 0
for match in re.finditer(r'(([\+\-]?\d+)|([Oo][Nn])|([Oo][Ff]{2})|=)', stdin):
    if match.group(1) == match.group(3) and not on:
        on = True
    elif match.group(1) == match.group(4):
        on = False
    elif match.group(1) == match.group(2) and on:
        sum += int(match.group(2))
    elif match.group(1) == "=":
        print(sum)
