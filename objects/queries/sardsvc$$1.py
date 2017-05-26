class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "SARDSVC$$1",
            "collections": [
                "SARD"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, device label, avserv value from SARD) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)