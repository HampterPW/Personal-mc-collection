import requests
from bs4 import BeautifulSoup

url = "https://vault.omniarchive.uk/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a")
    
    with open("index.html", "w") as f:
        f.write("<!DOCTYPE html>\n<html>\n<head><title>Fanmade Index</title></head>\n<body>\n")
        f.write("<h1>Fanmade Index for Vault</h1>\n<ul>\n")
        for link in links:
            href = link.get("href")
            f.write(f"<li><a href='{url}{href}'>{href}</a></li>\n")
        f.write("</ul>\n</body>\n</html>")
    print("Index created successfully.")
else:
    print(f"Failed to access the site. Status code: {response.status_code}")
