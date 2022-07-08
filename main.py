from mechanicalsoup import Browser
import pandas as pd

url = "https://www.amazon.in/gp/bestsellers/books/"
browser = Browser()
# Request page
page = browser.get(url)

# Reterving the beautifulsoup object
soup = page.soup

# Getting ranks (bestsellers)
div_ranks = soup.findAll("div", {"class" : "a-section zg-bdg-body zg-bdg-clr-body aok-float-left"})
ranks = [rank.getText() for rank in div_ranks]

# Getting prices
span_prices = soup.findAll("span", {"class":"p13n-sc-price"})
prices = [price.getText() for price in span_prices]

span_reviews = soup.findAll("span", {"class" : "a-icon-alt"})
reviews = [review.getText() for review in span_reviews]

# Getting titles & authors
div_titles_authors = soup.findAll("div", attrs={"class" : "_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y"})
authors = []
titles = []

for index, div in enumerate(div_titles_authors):
    if not index%2:
        titles.append(div.getText())
    else:
        authors.append(div.getText())
        
# Creat a dataframe for the books
books = {
    "Ranks" : ranks,
    "Titles" : titles,
    "Authors" : authors,
    "Reviwes" : reviews,
    "Prices" : prices
}
df = pd.DataFrame.from_dict(books, orient="index")
df = df.transpose()

