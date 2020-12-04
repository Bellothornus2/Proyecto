from .web_crawler import get_html
#This function gets the content inside the html tag that we specfied earlier
def css_class_get_content(page, string_key_class):
    #PRUEBA
    #this variable stores the html open tag  INT
    int_html_open_tag = page.rfind("<", 0, string_key_class - 1)
    #this variable stores the html tag  STR
    string_html_tag = page[int_html_open_tag + 1:string_key_class - 1]
    #this variable stores the start index of the content INT
    int_content_key_start = page.find('>', string_key_class) 
    #this variable stores the end index of the content INT
    int_content_key_end = page.find('</'+string_html_tag, int_content_key_start + 1)
    #this variable stores the content of the html tag STR
    string_content_key = page[int_content_key_start+1:int_content_key_end]
    page = page[int_content_key_end+1:]
    #PRUEBA
    return string_content_key, page
    
#This function gets the next id from the page at given position 
def css_class_finder(page,key,dict_class_html):
    #this search the class that we want and stores it in "string_key_class" 
    while True:
        string_key_class = page.find('class="' + key + '"')
        #if he dont find it then breaks the cycle
        if string_key_class == -1:
            break
        #if he finds it then find all the occurence of the page
        else:
            string_class_content, page = css_class_get_content(page, string_key_class)
            dict_class_html[key].append(string_class_content)
            continue
    return dict_class_html


#Here we take all the content of the pages
def get_all_content(list_links, list_class_html, dict_class_html):
    for url in list_links:
        page = get_html(url)
        for class_html in list_class_html:
            dict_class_html = css_class_finder(page,class_html, dict_class_html)
    return dict_class_html


