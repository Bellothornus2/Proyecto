from modules.web_crawler import get_all_pages
from modules.web_scraper import get_all_content
from modules.json.save_json import save_json_file


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
#este diccionario coge los registros de cada columna
dict_class_html = {
    "PricePack":[],
    "NamePack":[],
    "ContentPack":[],
    "HasCupon":[],
    "HasParking":[]
}
"""
dict_class_html_experimental = {
    "0":{
        "PricePack":"Price",
        "NamePack":"Name",
        "ContentPack":"Content"
    },
    "1":{
        "pricePack":"Price"
    }
}
"""
dict_class_html_experimental = {}
#list_links = get_all_pages(webpage=webpage)
#print(list_links)


#dict_class_html = get_all_content(list_links, list_class_html, dict_class_html)
dict_class_html =  get_all_content(["products.html"],list_class_html,dict_class_html)
#This function stores all the content of the pages in a json file per column
#save_json_file(get_all_content(get_all_pages(webpage=webpage),list_class_html,dict_class_html))
#this function stores all the content of the pages in a json file per pack
for i in range(len(dict_class_html)+1):
    dict_class_html_experimental[str(i)] = {}
    dict_class_html_experimental[str(i)]["PricePack"] = dict_class_html["PricePack"][i]
    dict_class_html_experimental[str(i)]["NamePack"] = dict_class_html["NamePack"][i]
    dict_class_html_experimental[str(i)]["ContentPack"] = dict_class_html["ContentPack"][i]
    dict_class_html_experimental[str(i)]["HasCupon"] = dict_class_html["HasCupon"][i]
    dict_class_html_experimental[str(i)]["HasParking"] = dict_class_html["HasParking"][i]

save_json_file(dict_class_html_experimental)


