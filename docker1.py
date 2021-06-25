#!/usr/bin/python3

import cgi
import subprocess
import time

print("content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()

# FieldStrorage is  a function to take input
f = cgi.FieldStorage()
cmd = f.getvalue("x")

# sudo power bcoz we are runnig docker commands
output = subprocess.getoutput("sudo " + cmd)
print(output)