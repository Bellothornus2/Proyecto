from modules.web_crawler import get_all_links, get_html, get_all_pages
from modules.web_scraper import css_class_finder
#we initialize the empty list "list_links" to store all the links here
#and the varaible string "string_url" to store the root of the content
#we initialize the dictionary who contains the ids of the elements that we want to store 
list_links = []
webpage="http://localhost:8000/html/"
string_url= "index.html"
list_class_html = [
    "PricePack",
    "NamePack",
    "ContentPack",
    "HasCupon",
    "HasParking"
]
dict_class_html = dict.fromkeys(list_class_html, [])

list_links = get_all_pages(webpage=webpage)
print(list_links)

#Here we take all the content of the pages
for url in list_links:
    page = get_html(url)
    for class_html in list_class_html:
        list_content = css_class_finder(page,class_html)
        if list_content != None:
            dict_class_html[class_html].append(list_content)
print(dict_class_html)