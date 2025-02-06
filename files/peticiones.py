import requests
import os

response = requests.get("https://google.es")
print(f"\n[+] Status code: {response.status_code}")

with open("index.html", "w") as file:
    file.write(response.text)