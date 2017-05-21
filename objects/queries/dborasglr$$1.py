class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGLR$$1",
            "collections": [
                "DBORASGLR"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, owner||' '||objtype||' '||object||' '||subobject label, gets value from DBORASGLR) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)