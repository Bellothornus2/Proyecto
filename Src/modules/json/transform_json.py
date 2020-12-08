def transorm_json_data(dict_class_html_experimental, dict_class_html):
    for i in range(len(dict_class_html)+1):
        dict_class_html_experimental[str(i)] = {}
        dict_class_html_experimental[str(i)]["PricePack"] = dict_class_html["PricePack"][i]
        dict_class_html_experimental[str(i)]["NamePack"] = dict_class_html["NamePack"][i]
        dict_class_html_experimental[str(i)]["ContentPack"] = dict_class_html["ContentPack"][i]
        dict_class_html_experimental[str(i)]["HasCupon"] = dict_class_html["HasCupon"][i]
        dict_class_html_experimental[str(i)]["HasParking"] = dict_class_html["HasParking"][i]
    return dict_class_html_experimental