from modules.web_crawler.get_all_pages import get_all_pages
from modules.web_scraper.get_all_content import get_all_content
from modules.json.transform_json import transform_json_data
from modules.json.save_json import save_json_file
from modules.json.save_atlas import save_atlas
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

#dict_class_html = get_all_content(get_all_pages(), list_class_html, dict_class_html)
dict_class_html =  get_all_content(["products.html"],list_class_html,dict_class_html)
#This function stores all the content of the pages in a json file per column
save_json_file(dict_class_html)

#this function stores all the content of the pages in a json file per pack
dict_class_html_experimental = {}
dict_class_html_experimental = transform_json_data(dict_class_html_experimental, dict_class_html, list_class_html)
save_json_file(dict_class_html_experimental)
save_atlas(dict_class_html_experimental)


