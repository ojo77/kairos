class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "EBSNODCHOICE",
            "collections": ["EBS12CM"],
            "request": "select distinct node_name as label from EBS12CM order by label"
        }
        super(UserObject, s).__init__(**object)