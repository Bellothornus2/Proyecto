#Here we import the library to download the HTMl
import urllib.request
from . import web_crawler
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

#This function is to download the HTMl in "UTF-8" Codification from a given URI
def gethtml(string_url,webpage="http://localhost:8000/html/"):
    try:
        request = urllib.request.urlopen(webpage + string_url)
    except:
        print(webpage + string_url)
    #si tiene el charset puesto:
    #html = request.read().decode(request.headers.get_content_charset())
    #si no:
    html = request.read().decode('utf-8')
    return html



def css_class_get_content(page, string_key_class):
    pass
    #PRUEBA
    #this variable stores the html open tag
    string_html_open_tag = page.rfind("<",0,string_key_class - 1)
    #this variable stores the html tag
    string_html_tag = page[string_html_open_tag:string_key_class]
    #this variable stores the start index of the content
    string_content_key_start = page.find('>', string_key_class) 
    #this variable stores the end index of the content
    string_content_key_end = page.find('</'+string_html_tag, string_content_key_start + 1)
    #this variable stores the content of the html tag
    string_content_key = page[string_content_key_start+1:string_content_key_end]
    #PRUEBA
    return string_content_key, string_

#This function gets the next id from the page at given position 
def css_class_finder(page,key):
    #this search the class that we want and stores it in "string_key_class" 
    string_key_class = page.find('class="' + key + '"')
    #if he dont find it then returns None 
    if string_key_class == -1:
        string_content_key = None
        
    #if he finds it then...
    else:
        css_class_get_content(page, string_key_class)
        """
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        string_class = page[start_quote + 1: end_quote]
        """




#Here we take all th links from the root level "index.html"
page = gethtml(string_url)
print_all_links(page)
print(list_links)

#Then here we take all the links from all the urls from the entire webpage recursively.
get_all_pages(list_links)
print(list_links)

for url in list_links:
    page = gethtml(url)
    for class_html in list_class_html:
        string_content = css_class_finder(page,class_html)
        dict_class_html[class_html].append(string_content)
    css_class_finder
