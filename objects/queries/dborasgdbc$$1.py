class UserObject(dict):
    def __init__(s):
        object = {
            "type": "query",
            "id": "DBORASGDBC$$1",
            "collections": [
                "DBORASGDBC"
            ],
            "userfunctions": [],
            "request": "select timestamp, label label, sum(value) value from (select timestamp, owner||' '||objtype||' '||object||' '||subobject label, changes value from DBORASGDBC) group by timestamp, label order by timestamp",
            "nocache": false,
            "filterable": true
        }
        super(UserObject, s).__init__(**object)