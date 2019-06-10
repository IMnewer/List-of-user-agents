import urllib.request

fp = urllib.request.urlopen("https://raw.githubusercontent.com/nu11secur1ty/List-of-user-agents/master/Chrome.txt")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)
