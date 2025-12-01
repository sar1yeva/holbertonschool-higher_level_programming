#!/usr/bin/python3
import urllib.request

url = "https://intranet.hbtn.io/status"

# URL-ə GET sorğusu göndərir və cavabı tab və tire ilə çap edir
with urllib.request.urlopen(url) as response:
    body = response.read().decode('utf-8')
    print("\t- {}".format(body))
