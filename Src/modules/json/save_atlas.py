import pymongo
#import dns
#Here we are connecting to the server
def save_atlas(dict_class_html_row):
    client = pymongo.MongoClient("mongodb+srv://m001-student:m001-mongodb-basics@sandbox.jhgbt.gcp.mongodb.net/admin?retryWrites=true&w=majority")
    #Here we are connecting to the database
    db = client.amenities
    #Here we are connecting to the collection
    collection = db.packs2
    #print(dict_class_html_row)
    #here we are inserting the retrieved data
    for key,value in dict_class_html_row.items():
        #print("{%s:%s}" % (key,value))
        
        collection.insert_one(value)