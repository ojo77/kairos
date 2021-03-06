class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAHELP",
            "collections": ["DBORAREQ"],
            "nocache": True,
            "request": "select distinct sqlid as key, request as value from DBORAREQ where sqlid = '%(DBORAHELP)s'"
        }
        super(UserObject, s).__init__(**object)