import urllib.request

url = "https://intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    data = response.read()
    print(data)
