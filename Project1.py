import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml
from urllib.parse import urljoin

# Initialize lists
BN = []
AN = []
RT = []
links = []
CON = []

# Send the request to the website
base_url = "https://www.abjjad.com"
SearchLink="https://www.abjjad.com/search?kw=%D9%85%D8%B5%D8%B7%D9%81%D9%89%20%D9%85%D8%AD%D9%85%D9%88%D8%AF"
result = requests.get(SearchLink)
cont = result.content
soup = BeautifulSoup(cont, "lxml")

# Extract book names, author names, ratings, and links
BookName = soup.find_all("h3", {"class": "summary-header"})
AuthotName = soup.find_all("span", {"class": "author"})
Rating = soup.find_all("span", {"class": "rating"})

# Populate the lists
for i in range(len(BookName)):
    BN.append(BookName[i].text.strip())
    AN.append(AuthotName[i].text.strip())
    RT.append(Rating[i].text.strip())
    
    # Correctly extract the link from the 'a' tag
    link_tag = BookName[i].find("a")
    if link_tag and 'href' in link_tag.attrs:
        full_link = urljoin(base_url, link_tag['href'])
        links.append(full_link)
    else:
        links.append('No Link')

# Fetch content for each link
for link in links:
    if link != 'No Link':
        result = requests.get(link)
        cont = result.content
        soup = BeautifulSoup(cont, "lxml")

        # Extract content for the book
        content_tags = soup.find_all("span", {"class": "content"})
        # Assuming each book has a single content element
        content_text = " ".join(tag.text.strip() for tag in content_tags)
        CON.append(content_text)
    else:
        CON.append('No Content')

# Create a DataFrame from the lists
df = pd.DataFrame({
    "Book Name": BN,
    "Author": AN,
    "Rating": RT,
    "Content": CON
})

# Save the DataFrame to an Excel file
excel_path = r"E:\COURSES\MO3TASEM\01Python\Projects\WEB_Scrabing\Data.xlsx"
df.to_excel(excel_path, index=False, engine='openpyxl')

print("Data has been successfully written to Data.xlsx")





