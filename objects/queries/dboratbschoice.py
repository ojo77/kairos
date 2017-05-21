class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORATBSCHOICE",
            "collections": ["DBORATBS"],
            "request": "select distinct tablespace label from DBORATBS order by label"
        }
        super(UserObject, s).__init__(**object)