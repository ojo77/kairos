class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASQC$$1",
            "collections": [
                "DBORASQC"
            ],
            "userfunctions": [],
            "request": "select timestamp, label as label, sum(value) as value from (select timestamp, sqlid as label, cpu as value from DBORASQC) as foo group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)