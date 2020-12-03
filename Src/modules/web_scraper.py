#TODO: We have to complete this NOW!
def css_class_get_content(page, string_key_class):
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
    return string_content_key, #string_
    
#This function gets the next id from the page at given position 
def css_class_finder(page,key):
    #this search the class that we want and stores it in "string_key_class" 
    string_key_class = page.find('class="' + key + '"')
    while True:
        #if he dont find it then returns None and breaks the cycle
        if string_key_class == -1:
            string_content_key = None
            break
        #if he finds it then find all the occurence of the page
        else:
            string_class_content = css_class_get_content(page, string_key_class)
            page = page[string_class_content+1:]
            """
            start_quote = page.find('"', start_link)
            end_quote = page.find('"', start_quote + 1)
            string_class = page[start_quote + 1: end_quote]
            """
            continue
