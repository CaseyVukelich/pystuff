import sys, urllib.request

url = input("Enter the URL: ")
x = urllib.request.urlopen(url, None)

print(x.read().decode())