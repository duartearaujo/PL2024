import sys
import re

template = """
<!DOCTYPE html>
<html>
<head>
    <title>TPC2</title>
    <meta charset="UTF-8">
</head>
<body>
"""

stdin = sys.stdin.read()
out = stdin

# Headers
out = re.sub(r'(?<!#)\s*# ([^\n]*)', r'<h1>\1</h1>', out)
out = re.sub(r'(?<!#)\s*[#]{2} ([^\n]*)', r'<h2>\1</h2>', out)
out = re.sub(r'(?<!#)\s*[#]{3} ([^\n]*)', r'<h3>\1</h3>', out)

# Bold
out = re.sub(r'\*\*([^\*]*)\*\*', r'<b>\1</b>', out)

# Italic
out = re.sub(r'\*([^\*]*)\*', r'<i>\1</i>', out)

# Lists
l = ""
ul = False
ol = False
for line in out.split("\n"):
    if re.match(r'^\d\.(.*)$', line):
        if not ol:
            l += "<ol>\n"
            ol = True
        line = re.sub(r'^\s*\d+\.(.*)$', r'<li>\1</li>', line)
        l += line + "\n"
    elif re.match(r'^\s*-(.*)$', line):
        if not ul:
            l += "<ul>\n"
            ul = True
        line = re.sub(r'^\s*-(.*)$', r'<li>\1</li>', line)
        l += line + "\n"
    else:
        if ul:
            l += "</ul>\n"
            ul = False
        if ol:
            l += "</ol>\n"
            ol = False
        l += line + "\n"

out = l

# Images
out = re.sub(r'!\[(.*)\]\((.*)\)', r'<img src="\2" alt="\1">', out)

# Links
out = re.sub(r'\[(.*)\]\((.*)\)', r'<a href="\2">\1</a>', out)

template += out
template += "</body>\n"
template += "</html>\n"

with open("output.html", "w") as f:
    f.write(template)




