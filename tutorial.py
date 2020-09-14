import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
#opening up connection grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#parsing html
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div",{"class":"item-info"})

for container in containers:
    brand = container.img["title"]
    
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text
    
    shipping_container = container.findAll("li", {"class":"price-ship"})
    
    print("brand: " + brand)
    print("product: " + product_name)
                                           