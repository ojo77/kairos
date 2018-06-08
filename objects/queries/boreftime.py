class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "BOREFTIME",
            "collections": ["BO"],
            "request": "select distinct timestamp from BO"
        }
        super(UserObject, s).__init__(**object)