from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.amazon.in/gp/bestsellers/books/"
page = urlopen(url)
html_text = page.read().decode("utf-8")
soup = BeautifulSoup(html_text, "html.parser")
div_tag = soup.find_all("div", {"class": "_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y"})

# for link in soup.select("a"):
#     try:
#         print(link['span'])
#     except:
#         print("NO span")
for tag in div_tag:
    print(tag.text)