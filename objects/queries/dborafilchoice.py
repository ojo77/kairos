class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAFILCHOICE",
            "collections": ["DBORAFIL"],
            "request": "select distinct file as label from DBORAFIL order by label"
        }
        super(UserObject, s).__init__(**object)