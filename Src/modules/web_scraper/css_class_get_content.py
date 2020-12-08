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
    
    if string_content_key == "No Coupon" or string_content_key == "No Parking":
        string_content_key = False
    elif string_content_key == "Parking: Yes" or string_content_key == "Coupon: Yes":
        string_content_key = True
    return string_content_key, page