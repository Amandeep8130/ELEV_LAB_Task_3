import requests
from bs4 import BeautifulSoup

# Step 1: Fetch HTML
url = "https://www.hindustantimes.com/"
response = requests.get(url)
html_content = response.text

# Step 2: Parse the HTML for <h2> or <title> tags
soup = BeautifulSoup(html_content, "html.parser")

titles = []

# Extract all <h2> tags
for h2 in soup.find_all("h2"):
    text = h2.get_text(strip=True)
    if text:
        titles.append(text)

# Safe extraction of <title>
if soup.title:
    page_title = soup.title.get_text(strip=True)
else:
    page_title = "No title found"

titles.insert(0, page_title)

# Step 3: Save titles in a .txt file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for t in titles:
        file.write(t + "\n")

print("Headlines saved to headlines.txt")
