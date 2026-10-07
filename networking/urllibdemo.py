from urllib.error import HTTPError
from urllib.request import urlopen

try:
    url = urlopen("http://www.python.org/")
    content = url.read()
except HTTPError:
    print("The webpage not found.")
    exit()

f = open("python.html", 'wb')
f.write(content)
f.close()