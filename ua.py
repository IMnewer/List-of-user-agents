#!/usr/bin/python3
import urllib.request

row = urllib.request.urlopen("https://raw.githubusercontent.com/nu11secur1ty/List-of-user-agents/master/Chrome.txt")
mylists = row.read()

mystr = mylists.decode("utf8")
row.close()

print(mystr)

rowb = urllib.request.urlopen("https://raw.githubusercontent.com/nu11secur1ty/List-of-user-agents/master/Firefox.txt")
mylistsb = rowb.read()

mystrb = mylistsb.decode("utf8")
rowb.close()

print(mystrb)

