from pymongo import MongoClient
from bson import ObjectId
import json

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

class Links:
    def __init__(self):
        self.cli = MongoClient()
        self.db = self.cli["links"]

    def set_link(self,link,language):
        try:
            self.db.insert_one({"link":link,"language":language})
        except:
            return False

    def get_links(self):

        return self.db.find()



    def all(self):
        link_json = []
        all_datas = self.db["links"].find()
        for data in all_datas:
            del data["_id"]
            link_json.append(data)

        return JSONEncoder().encode(link_json)


    def search(self,cat=None,content=None):

        searched_links = self.db.links.find({'{}'.format(str(cat).lower()):{"$regex": u"{}".format(content.replace(" ",""))}})
        search_arr = []
        for s_link in searched_links:
            del s_link['_id']
            search_arr.append(s_link)

        return JSONEncoder().encode(search_arr)

