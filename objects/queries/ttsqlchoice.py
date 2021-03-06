class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "TTSQLCHOICE",
            "collections": ["TTSQLHS"],
            "request": "select distinct hashid as label from TTSQLHS order by label"
        }
        super(UserObject, s).__init__(**object)