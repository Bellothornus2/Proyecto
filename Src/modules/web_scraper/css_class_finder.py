from .css_class_get_content import css_class_get_content
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