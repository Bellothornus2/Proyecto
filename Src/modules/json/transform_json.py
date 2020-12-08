def transform_json_data(dict_class_html_experimental, dict_class_html, list_class_html):
    for x in dict_class_html:
        first_index=x
        break
    for i in range(len(dict_class_html[first_index])):
        dict_class_html_experimental[str(i)] = {}
        for x in list_class_html:
            dict_class_html_experimental[str(i)][x] = dict_class_html[x][i]
    return dict_class_html_experimental