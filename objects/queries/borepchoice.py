class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "BOREPCHOICE",
            "collections": ["BO"],
            "request": "select distinct report as label from BO order by label"
        }
        super(UserObject, s).__init__(**object)