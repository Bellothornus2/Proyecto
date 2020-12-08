def pretty_json_homemade(dict_class_html):
    data = str(dict_class_html)
    data = data.replace("],","],\n")
    data = data.replace("[","[\n\t")
    data = data.replace("',","',\n\t")
    data = data.replace("'],","'\n],")
    data = data.replace("']","'\n]")
    data = data.replace("{","{\n")
    data = data.replace("}","\n}")
    return data