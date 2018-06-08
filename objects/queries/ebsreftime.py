class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSREFTIME",
            "collections": ["EBS12CM"],
            "request": "select distinct timestamp from EBS12CM"
        }
        super(UserObject, s).__init__(**object)