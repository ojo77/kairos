class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORAASHSQLCHOICE",
            "collections": ["ORAHAS"],
            "request": "select distinct sql_id as label from ORAHAS where sql_id != '' order by label"
        }
        super(UserObject, s).__init__(**object)