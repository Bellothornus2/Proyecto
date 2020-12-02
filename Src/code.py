from .web_crawler import get_all_links, gethtml, get_all_pages
from .web_scraper import css_class_finder
#we initialize the empty list "list_links" to store all the links here
#and the varaible string "string_url" to store the root of the content
#we initialize the dictionary who contains the ids of the elements that we want to store 
list_links = []
string_url= "index.html"
list_class_html = [
    "PricePack",
    "NamePack",
    "ContentPack",
    "HasCupon",
    "HasParking"
]
dict_class_html = dict.fromkeys(list_class_html, [])

#Here we take all th links from the root level "index.html"
page = gethtml(string_url)
get_all_links(page, list_links)
print(list_links)

#Then here we take all the links from all the urls from the entire webpage recursively.
get_all_pages(list_links)
print(list_links)

#Here
for url in list_links:
    page = gethtml(url)
    for class_html in list_class_html:
        string_content = css_class_finder(page,class_html)
        dict_class_html[class_html].append(string_content)
print(dict_class_html)
