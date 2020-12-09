import json
import datetime

def save_json_file(dict_class_html):
    name_file = datetime.datetime.now().strftime("%d%m%y_%H%M%S.%f")[:-3]
    with open('../database/' + name_file + '.json', 'w') as fp:
        json.dump(dict_class_html, fp, indent=4, sort_keys=True)
    